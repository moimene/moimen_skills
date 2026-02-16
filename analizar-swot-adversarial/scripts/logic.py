"""
Litigation SWOT Adversarial Analysis

Ejecuta análisis adversarial de escritos procesales mediante segmentación
inteligente y bucle de inferencia LLM local.

Author: Legal Engineering Dept.
Version: 1.0.2
"""

import json
import re
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Optional


# ═══════════════════════════════════════════════════════════════════════════════
# TYPES & ENUMS
# ═══════════════════════════════════════════════════════════════════════════════

class Severity(Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class AnalysisMode(Enum):
    ADVERSARIAL = "ADVERSARIAL"
    SELF_AUDIT = "SELF_AUDIT"
    COMPARATIVE = "COMPARATIVE"


@dataclass
class Finding:
    """Representa un hallazgo individual del análisis."""
    segment_id: int
    text_snippet: str
    weakness_severity: Severity
    fallacy_detected: Optional[str] = None
    fallacy_quote: Optional[str] = None
    evidentiary_gap: Optional[str] = None
    contradiction_with: Optional[int] = None
    legal_basis: Optional[str] = None
    counter_argument_suggestion: str = ""


@dataclass
class SWOTMatrix:
    """Matriz DAFO estratégica."""
    strengths: list = field(default_factory=list)   # S - Fortalezas del contrario
    weaknesses: list = field(default_factory=list)  # W - Debilidades explotables
    opportunities: list = field(default_factory=list)  # O - Huecos probatorios
    threats: list = field(default_factory=list)     # T - Amenazas para nosotros


# ═══════════════════════════════════════════════════════════════════════════════
# DOCUMENT LOADING (Stub - Implementar con librería real)
# ═══════════════════════════════════════════════════════════════════════════════

class DocumentLoader:
    """Cargador seguro de documentos en Enclave."""
    
    @staticmethod
    def load_secure(file_path: str) -> str:
        """
        Carga documento de forma segura sin conexión a red.
        
        En producción, usar:
        - PyMuPDF para PDF
        - python-docx para DOCX
        - Tesseract local para OCR si es necesario
        """
        path = Path(file_path)
        
        if path.suffix.lower() == '.txt':
            return path.read_text(encoding='utf-8')
        
        elif path.suffix.lower() == '.pdf':
            # Placeholder - En producción usar PyMuPDF
            try:
                import fitz  # PyMuPDF
                doc = fitz.open(file_path)
                text = ""
                for page in doc:
                    text += page.get_text()
                return text
            except ImportError:
                raise RuntimeError("PyMuPDF (fitz) no instalado. Ejecutar: pip install pymupdf")
        
        elif path.suffix.lower() in ['.docx', '.doc']:
            # Placeholder - En producción usar python-docx
            try:
                from docx import Document
                doc = Document(file_path)
                return "\n".join([para.text for para in doc.paragraphs])
            except ImportError:
                raise RuntimeError("python-docx no instalado. Ejecutar: pip install python-docx")
        
        else:
            raise ValueError(f"Formato no soportado: {path.suffix}")


# ═══════════════════════════════════════════════════════════════════════════════
# SEGMENTATION
# ═══════════════════════════════════════════════════════════════════════════════

def split_by_legal_paragraphs(text: str) -> list[tuple[int, str]]:
    """
    Segmenta el texto por párrafos lógicos legales.
    
    Detecta patrones como:
    - HECHO PRIMERO, HECHO SEGUNDO, etc.
    - PRIMERO.-, SEGUNDO.-, etc.
    - I.-, II.-, III.-, etc.
    - Párrafos numerados: 1., 2., 3.
    
    Returns:
        Lista de tuplas (segment_id, texto_del_segmento)
    """
    # Patrones de inicio de sección legal
    patterns = [
        r'(?:HECHO\s+)?(?:PRIMERO|SEGUNDO|TERCERO|CUARTO|QUINTO|SEXTO|SÉPTIMO|OCTAVO|NOVENO|DÉCIMO|UNDÉCIMO|DUODÉCIMO|DECIMOTERCERO|DECIMOCUARTO|DECIMOQUINTO)',
        r'(?:FUNDAMENTO\s+)?(?:PRIMERO|SEGUNDO|TERCERO|CUARTO|QUINTO)',
        r'^[IVXLCDM]+\.?\-?\s',  # Numeración romana
        r'^\d+\.?\-?\s',  # Numeración arábiga
        r'^[A-Z]\)\s',  # Letras con paréntesis
    ]
    
    combined_pattern = '|'.join(f'({p})' for p in patterns)
    
    # Dividir por patrones
    segments = []
    current_segment = []
    segment_id = 0
    
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        # Detectar inicio de nuevo segmento
        if re.match(combined_pattern, line, re.IGNORECASE | re.MULTILINE):
            if current_segment:
                segments.append((segment_id, ' '.join(current_segment)))
                segment_id += 1
            current_segment = [line]
        else:
            current_segment.append(line)
    
    # Añadir último segmento
    if current_segment:
        segments.append((segment_id, ' '.join(current_segment)))
    
    # Si no se detectaron patrones, dividir por párrafos dobles
    if len(segments) <= 1:
        paragraphs = re.split(r'\n\s*\n', text)
        segments = [(i, p.strip()) for i, p in enumerate(paragraphs) if p.strip()]
    
    return segments


# ═══════════════════════════════════════════════════════════════════════════════
# LLM INFERENCE (Stub - Implementar con modelo local)
# ═══════════════════════════════════════════════════════════════════════════════

class LocalLLM:
    """Wrapper para inferencia LLM local."""
    
    def __init__(self, model_path: Optional[str] = None):
        self.model_path = model_path
        self.system_prompt = self._load_system_prompt()
    
    def _load_system_prompt(self) -> str:
        """Carga el system prompt desde archivo."""
        prompt_path = Path(__file__).parent.parent / "resources" / "system_prompt.md"
        if prompt_path.exists():
            return prompt_path.read_text(encoding='utf-8')
        return ""
    
    def generate(
        self,
        user_input: str,
        temperature: float = 0.2,
        max_tokens: int = 1024
    ) -> str:
        """
        Genera respuesta del LLM.
        
        En producción, implementar con:
        - llama.cpp para Llama/Mixtral local
        - vLLM para inferencia optimizada
        - Ollama para gestión de modelos
        """
        # Placeholder - En producción, llamar al modelo real
        # Ejemplo con Ollama:
        #
        # import ollama
        # response = ollama.generate(
        #     model='llama3:70b-instruct',
        #     system=self.system_prompt,
        #     prompt=user_input,
        #     options={'temperature': temperature}
        # )
        # return response['response']
        
        raise NotImplementedError(
            "Implementar inferencia LLM local. "
            "Ver comentarios para ejemplos con Ollama, llama.cpp, o vLLM."
        )


# ═══════════════════════════════════════════════════════════════════════════════
# SWOT CATEGORIZATION
# ═══════════════════════════════════════════════════════════════════════════════

def categorize_findings(findings: list[Finding]) -> SWOTMatrix:
    """
    Categoriza los hallazgos en matriz DAFO.
    
    Lógica de clasificación:
    - Si hay déficit probatorio → OPORTUNIDAD (podemos impugnar)
    - Si hay falacia → DEBILIDAD del contrario
    - Si detectamos punto fuerte documentado → FORTALEZA (defensa difícil)
    - Si hay riesgo para nuestro caso → AMENAZA
    """
    swot = SWOTMatrix()
    
    for finding in findings:
        # Filtrar baja severidad
        if finding.weakness_severity == Severity.LOW:
            continue
        
        snippet_preview = finding.text_snippet[:80] + "..." if len(finding.text_snippet) > 80 else finding.text_snippet
        
        # OPORTUNIDADES: Déficit probatorio explotable
        if finding.evidentiary_gap:
            opportunity = {
                "segment": finding.segment_id,
                "type": "Déficit Probatorio",
                "description": finding.evidentiary_gap,
                "action": finding.counter_argument_suggestion,
                "legal_basis": finding.legal_basis
            }
            swot.opportunities.append(opportunity)
        
        # DEBILIDADES: Falacias argumentativas
        if finding.fallacy_detected:
            weakness = {
                "segment": finding.segment_id,
                "fallacy": finding.fallacy_detected,
                "quote": finding.fallacy_quote or snippet_preview,
                "action": finding.counter_argument_suggestion
            }
            swot.weaknesses.append(weakness)
        
        # AMENAZAS: Puntos que nos perjudican
        # (Esto requiere análisis adicional - marcado manual o detección de fortalezas)
        if "riesgo" in finding.counter_argument_suggestion.lower() or \
           "perjudica" in finding.counter_argument_suggestion.lower():
            threat = {
                "segment": finding.segment_id,
                "description": snippet_preview,
                "risk_level": finding.weakness_severity.value
            }
            swot.threats.append(threat)
    
    return swot


# ═══════════════════════════════════════════════════════════════════════════════
# REPORT GENERATION
# ═══════════════════════════════════════════════════════════════════════════════

def generate_report(swot: SWOTMatrix, findings: list[Finding]) -> dict:
    """Genera el informe final estructurado."""
    
    # Resumen ejecutivo
    executive_summary = []
    
    if swot.opportunities:
        executive_summary.append(
            f"✅ {len(swot.opportunities)} oportunidades de impugnación por déficit probatorio"
        )
    
    if swot.weaknesses:
        executive_summary.append(
            f"⚠️ {len(swot.weaknesses)} falacias argumentativas detectadas"
        )
    
    if swot.threats:
        executive_summary.append(
            f"🚨 {len(swot.threats)} puntos de riesgo que requieren defensa activa"
        )
    
    # Action items priorizados
    action_items = []
    
    # Prioridad 1: Impugnaciones por falta de prueba
    for opp in swot.opportunities:
        action_items.append({
            "priority": 1,
            "type": "IMPUGNAR",
            "segment": opp["segment"],
            "action": opp["action"]
        })
    
    # Prioridad 2: Uso de falacias para desacreditar
    for weak in swot.weaknesses:
        action_items.append({
            "priority": 2,
            "type": "EXPONER_FALACIA",
            "segment": weak["segment"],
            "action": weak["action"]
        })
    
    return {
        "executive_summary": executive_summary,
        "swot_matrix": {
            "strengths": swot.strengths,
            "weaknesses": swot.weaknesses,
            "opportunities": swot.opportunities,
            "threats": swot.threats
        },
        "findings_detail": [
            {
                "segment_id": f.segment_id,
                "text_snippet": f.text_snippet,
                "analysis": {
                    "weakness_severity": f.weakness_severity.value,
                    "fallacy_detected": f.fallacy_detected,
                    "evidentiary_gap": f.evidentiary_gap,
                    "counter_argument_suggestion": f.counter_argument_suggestion
                }
            }
            for f in findings
            if f.weakness_severity != Severity.LOW
        ],
        "action_items": sorted(action_items, key=lambda x: x["priority"]),
        "metadata": {
            "total_segments_analyzed": len(findings),
            "high_severity_count": sum(1 for f in findings if f.weakness_severity == Severity.HIGH),
            "medium_severity_count": sum(1 for f in findings if f.weakness_severity == Severity.MEDIUM)
        }
    }


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN EXECUTION
# ═══════════════════════════════════════════════════════════════════════════════

def execute_skill(
    file_path: str,
    mode: AnalysisMode = AnalysisMode.ADVERSARIAL,
    temperature: float = 0.2,
    severity_threshold: Severity = Severity.MEDIUM
) -> dict:
    """
    Ejecuta el análisis adversarial completo.
    
    Args:
        file_path: Ruta al documento a analizar
        mode: Modo de análisis (ADVERSARIAL, SELF_AUDIT, COMPARATIVE)
        temperature: Temperatura del LLM (0.1-0.3 recomendado)
        severity_threshold: Severidad mínima para incluir en informe
        
    Returns:
        Diccionario con matriz SWOT, hallazgos y recomendaciones
    """
    # 1. INGESTA SEGURA
    print(f"📄 Cargando documento: {file_path}")
    full_text = DocumentLoader.load_secure(file_path)
    print(f"   └─ Longitud: {len(full_text)} caracteres")
    
    # 2. SEGMENTACIÓN INTELIGENTE
    print("✂️  Segmentando por párrafos legales...")
    segments = split_by_legal_paragraphs(full_text)
    print(f"   └─ {len(segments)} segmentos detectados")
    
    # 3. BUCLE ADVERSARIAL
    print("🔍 Iniciando análisis adversarial...")
    llm = LocalLLM()
    findings: list[Finding] = []
    
    for segment_id, segment_text in segments:
        print(f"   └─ Analizando segmento {segment_id + 1}/{len(segments)}")
        
        try:
            # Invocar al LLM
            response = llm.generate(
                user_input=segment_text,
                temperature=temperature
            )
            
            # Parsear respuesta JSON
            finding_data = json.loads(response)
            
            # Construir Finding
            finding = Finding(
                segment_id=finding_data.get('segment_id', segment_id),
                text_snippet=finding_data.get('text_snippet', segment_text[:200]),
                weakness_severity=Severity(finding_data['analysis']['weakness_severity']),
                fallacy_detected=finding_data['analysis'].get('fallacy_detected'),
                fallacy_quote=finding_data['analysis'].get('fallacy_quote'),
                evidentiary_gap=finding_data['analysis'].get('evidentiary_gap'),
                contradiction_with=finding_data['analysis'].get('contradiction_with'),
                legal_basis=finding_data['analysis'].get('legal_basis'),
                counter_argument_suggestion=finding_data['analysis'].get('counter_argument_suggestion', '')
            )
            
            # Filtrar por severidad
            severity_order = {Severity.LOW: 0, Severity.MEDIUM: 1, Severity.HIGH: 2}
            if severity_order[finding.weakness_severity] >= severity_order[severity_threshold]:
                findings.append(finding)
                
        except json.JSONDecodeError as e:
            print(f"      ⚠️ Error parseando respuesta del segmento {segment_id}: {e}")
        except Exception as e:
            print(f"      ⚠️ Error en segmento {segment_id}: {e}")
    
    print(f"\n📊 Análisis completado: {len(findings)} hallazgos relevantes")
    
    # 4. GENERACIÓN DE DAFO
    print("📋 Generando matriz DAFO...")
    swot_matrix = categorize_findings(findings)
    
    # 5. GENERAR INFORME
    report = generate_report(swot_matrix, findings)
    print("✅ Informe generado exitosamente")
    
    return report


# ═══════════════════════════════════════════════════════════════════════════════
# CLI ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Uso: python logic.py <ruta_al_documento>")
        print("Ejemplo: python logic.py demanda.pdf")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    try:
        result = execute_skill(file_path)
        print("\n" + "=" * 60)
        print("RESULTADO DEL ANÁLISIS")
        print("=" * 60)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
