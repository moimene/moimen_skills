"""
Context Manager - Gestión de Estado Compartido entre Agentes

Implementación de referencia basada en:
https://github.com/wshobson/agents/blob/main/plugins/agent-orchestration/agents/context-manager.md
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
import json


@dataclass
class ContextEntry:
    """Entrada individual en el contexto."""
    key: str
    value: Any
    timestamp: datetime = field(default_factory=datetime.now)
    source_agent: str = ""
    priority: int = 1  # 1-10, donde 10 es crítico
    ttl_seconds: Optional[int] = None  # Time to live


class ContextManager:
    """
    Gestor centralizado de contexto para sistemas multi-agente.
    
    Responsabilidades:
    - Mantener estado global coherente
    - Sincronizar información entre agentes
    - Resolver conflictos de información
    - Optimizar uso de tokens mediante compresión
    """
    
    def __init__(self, max_entries: int = 100, max_tokens: int = 4000):
        self.max_entries = max_entries
        self.max_tokens = max_tokens
        
        # Storage
        self.short_term_memory: Dict[str, ContextEntry] = {}
        self.long_term_memory: Dict[str, ContextEntry] = {}
        
        # Tracking
        self.access_history: List[str] = []
        self.conflict_log: List[Dict] = []
    
    def update_context(
        self,
        key: str,
        value: Any,
        source_agent: str,
        priority: int = 1,
        ttl_seconds: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Actualiza el contexto con nueva información.
        
        Args:
            key: Identificador de la entrada
            value: Valor de la entrada
            source_agent: Agente que genera la información
            priority: Prioridad 1-10
            ttl_seconds: Tiempo de vida en segundos (None = permanente)
        
        Returns:
            Estado actualizado del contexto
        """
        entry = ContextEntry(
            key=key,
            value=value,
            source_agent=source_agent,
            priority=priority,
            ttl_seconds=ttl_seconds
        )
        
        # Detectar conflictos
        if key in self.short_term_memory:
            existing = self.short_term_memory[key]
            if existing.value != value:
                self._handle_conflict(existing, entry)
        
        # Almacenar
        self.short_term_memory[key] = entry
        
        # Comprimir si excede límites
        if len(self.short_term_memory) > self.max_entries:
            self._prune_stale_context()
        
        return self.get_current_state()
    
    def get_context(self, key: str) -> Optional[Any]:
        """Recupera valor del contexto."""
        # Registrar acceso
        self.access_history.append(key)
        
        # Buscar en short-term
        if key in self.short_term_memory:
            return self.short_term_memory[key].value
        
        # Buscar en long-term
        if key in self.long_term_memory:
            return self.long_term_memory[key].value
        
        return None
    
    def broadcast_to_agents(
        self,
        message: Dict[str, Any],
        target_agents: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Broadcast de cambio de contexto a agentes afectados.
        
        Args:
            message: Mensaje a difundir
            target_agents: Lista de agentes destino (None = todos)
        
        Returns:
            Confirmación de broadcast
        """
        broadcast_log = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "targets": target_agents or "all_agents",
            "status": "broadcasted"
        }
        
        return broadcast_log
    
    def _handle_conflict(
        self,
        existing: ContextEntry,
        new: ContextEntry
    ) -> ContextEntry:
        """
        Resuelve conflicto entre dos entradas.
        
        Estrategias:
        1. Latest update wins (por defecto)
        2. Higher priority wins
        3. Higher authority agent wins
        """
        # Log del conflicto
        conflict = {
            "timestamp": datetime.now().isoformat(),
            "key": existing.key,
            "existing_value": existing.value,
            "existing_source": existing.source_agent,
            "new_value": new.value,
            "new_source": new.source_agent,
            "resolution": None
        }
        
        # Estrategia de resolución
        if new.priority > existing.priority:
            winner = new
            conflict["resolution"] = "priority_based"
        elif new.timestamp > existing.timestamp:
            winner = new
            conflict["resolution"] = "latest_wins"
        else:
            winner = existing
            conflict["resolution"] = "keep_existing"
        
        self.conflict_log.append(conflict)
        return winner
    
    def _prune_stale_context(self):
        """
        Elimina contexto obsoleto o de baja prioridad.
        
        Estrategia:
        1. Eliminar entradas expiradas (TTL)
        2. Mover a long-term las de alta prioridad
        3. Eliminar las menos accedidas
        """
        now = datetime.now()
        
        # 1. Eliminar expiradas
        expired_keys = []
        for key, entry in self.short_term_memory.items():
            if entry.ttl_seconds:
                age = (now - entry.timestamp).total_seconds()
                if age > entry.ttl_seconds:
                    expired_keys.append(key)
        
        for key in expired_keys:
            del self.short_term_memory[key]
        
        # 2. Mover de alta prioridad a long-term
        high_priority = {
            k: v for k, v in self.short_term_memory.items()
            if v.priority >= 7
        }
        
        for key, entry in high_priority.items():
            self.long_term_memory[key] = entry
        
        # 3. Eliminar menos accedidas si aún excede
        if len(self.short_term_memory) > self.max_entries:
            # Ordenar por frecuencia de acceso
            access_freq = {}
            for key in self.short_term_memory.keys():
                access_freq[key] = self.access_history.count(key)
            
            sorted_keys = sorted(
                access_freq.items(),
                key=lambda x: x[1]
            )
            
            # Eliminar los menos accedidos
            to_remove = len(self.short_term_memory) - self.max_entries
            for key, _ in sorted_keys[:to_remove]:
                if key not in high_priority:
                    del self.short_term_memory[key]
    
    def compress_context(self) -> str:
        """
        Comprime contexto a formato string optimizado.
        
        Returns:
            Representación comprimida del contexto
        """
        # Ordenar por prioridad
        sorted_entries = sorted(
            self.short_term_memory.values(),
            key=lambda x: x.priority,
            reverse=True
        )
        
        # Construir resumen
        summary_parts = []
        for entry in sorted_entries:
            summary_parts.append(
                f"{entry.key}: {entry.value} "
                f"(priority: {entry.priority}, "
                f"source: {entry.source_agent})"
            )
        
        return "\n".join(summary_parts)
    
    def get_current_state(self) -> Dict[str, Any]:
        """Retorna estado actual completo del contexto."""
        return {
            "short_term": {
                k: v.value
                for k, v in self.short_term_memory.items()
            },
            "long_term": {
                k: v.value
                for k, v in self.long_term_memory.items()
            },
            "metadata": {
                "total_entries": len(self.short_term_memory),
                "conflicts_count": len(self.conflict_log),
                "last_update": datetime.now().isoformat()
            }
        }
    
    def get_metrics(self) -> Dict[str, float]:
        """Calcula métricas de performance del Context Manager."""
        total_entries = (
            len(self.short_term_memory) + len(self.long_term_memory)
        )
        
        # Context Retention Rate
        retention_rate = (
            len(self.long_term_memory) / max(total_entries, 1)
        )
        
        # Conflict Resolution Rate
        conflicts_resolved = len([
            c for c in self.conflict_log
            if c["resolution"] is not None
        ])
        conflict_rate = (
            conflicts_resolved / max(len(self.conflict_log), 1)
        )
        
        return {
            "retention_rate": retention_rate,
            "conflict_resolution_rate": conflict_rate,
            "total_entries": total_entries,
            "conflicts_count": len(self.conflict_log)
        }


# Ejemplo de uso
if __name__ == "__main__":
    cm = ContextManager()
    
    # Agent A actualiza contexto
    cm.update_context(
        key="user_preference",
        value="dark_mode",
        source_agent="PreferenceAgent",
        priority=8
    )
    
    # Agent B actualiza el mismo contexto (conflicto)
    cm.update_context(
        key="user_preference",
        value="light_mode",
        source_agent="UIAgent",
        priority=5
    )
    
    # Verificar resolución
    state = cm.get_current_state()
    print(json.dumps(state, indent=2))
    
    # Métricas
    metrics = cm.get_metrics()
    print("\nMétricas:")
    print(json.dumps(metrics, indent=2))
