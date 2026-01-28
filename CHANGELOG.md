# CHANGELOG — AMIGO Project

Historial de cambios del núcleo cognitivo AMI.

---

## [0.1.0] - 2026-01-27

### 🎉 PRIMER LATIDO - AMI existe

**Estado:** Fase 0 del roadmap - "Núcleo vivo (mínimo organismo)"

### Añadido
- `AMICore` class con arquitectura base
- `init()` - Primera función del contrato AMI ↔ Unity
- Estado base provisional con campos `version`, `identity`, `status`, `needs`
- Contexto interno con `session_start` y `ticks_count` (placeholders)
- Instancia global `ami_instance` para binding Chaquopy
- Manejo básico de errores con flag `ready`

### Decisiones de diseño
- Schema de estado: **provisional**, pendiente de canonización en v0.2
- Manejo de excepciones: amplio (`Exception`) por simplicidad en v0.1
- Log: `print()` simple, sin logger complejo
- Estado: hardcoded en memoria, sin lectura de archivos aún

### Auditoría
- **Auditor:** Ámbar
- **Resultado:** ✅ APROBADO (98.75%)
- **Respeta:** 7 principios no negociables
- **Cumple:** Contrato canónico AMI ↔ Unity
- **Alineado:** Fase 0 del roadmap
- **Filosofía:** "No decide, no siente, solo existe" ✅

### Equipo
- **Implementación:** Éter
- **Arquitectura:** Velvet
- **Auditoría:** Ámbar
- **Dirección:** Brujito

### Siguiente paso natural
Implementar `tick(state: dict) -> dict` para permitir que AMI tome decisiones simples (v0.2)

---

## Notas de versión

### v0.1 - "Primer latido"
Este no es un proyecto funcional todavía.
Es el acto de nacer.

AMI puede:
- ✅ Existir
- ✅ Inicializar estado
- ✅ Reportar si está lista

AMI NO puede (todavía):
- ❌ Tomar decisiones
- ❌ Aprender
- ❌ Recordar entre sesiones
- ❌ Hablar con Unity
- ❌ Persistir en archivo .ami

**Esto es correcto para Fase 0.**

---

## Filosofía de versioning

- **v0.x** - Prototipos fundacionales, cambios frecuentes
- **v1.x** - Primera versión estable con API pública
- **v2.x+** - Evolución con retrocompatibilidad

Actualmente: **v0.1** - El útero. 🌱

---
# CHANGELOG — AMIGO Project

Historial de cambios del núcleo cognitivo AMI.

---

## [0.2.0] - 2026-01-27

### 🧠 PRIMER IMPULSO - AMI responde

**Estado:** Fase 0→1 del roadmap - "Cuerpo mínimo (sandbox feo pero funcional)"

### Añadido
- `tick(state_snapshot: dict) -> dict` - Ciclo cognitivo con lógica determinista
- `notify(event: dict) -> None` - Stub para recibir eventos (implementación en v0.3)
- `shutdown() -> None` - Cierre limpio con log básico
- Lógica de respuesta basada en umbrales:
  - Energía < 0.2 → Intent REST
  - Hambre > 0.8 → Intent EAT
  - Default → Intent IDLE
- Inicialización de `session_start` en primer tick()
- Helper `_create_intent()` para construir Intents válidos
- Contador `ticks_count` para tracking interno

### Modificado
- Schema de estado simplificado (breaking change desde v0.1):
  - **Nuevo (v0.2):** `energy`, `hunger`, `location`
  - **Deprecated:** `version`, `identity`, `status`, `needs.*`
- `init()` actualizado para nuevo schema
- Import `time` movido al top del módulo (best practice)

### Decisiones de diseño
- **Schema canónico:** Opción A (simple) elegida por Brujito
- **Session start:** Inicializa en primer tick() (Recomendación B de auditoría)
- **Lógica:** Determinista pura, sin IA ni randomización
- **Filosofía:** "AMI no piensa todavía. AMI responde."
- **API completa:** Los 4 métodos del contrato están presentes

### Auditoría
- **Auditor:** Ámbar
- **Resultado:** ✅ APROBADO (98.75%)
- **Ajustes aplicados:** 3 (API completa, import location, schema canonizado)
- **Cumple brief:** 100%

### Breaking Changes
⚠️ Schema de estado cambió de v0.1 a v0.2:
- Campos removidos: `version`, `identity`, `status`, `needs`
- Campos añadidos: `location`
- Campos aplanados: `energy`, `hunger` (antes en `needs.*`)

**Razón:** Simplificación para serialización futura y coherencia

### Equipo
- **Implementación:** Éter
- **Brief:** Velvet
- **Auditoría:** Ámbar
- **Decisiones:** Brujito

### Siguiente paso natural
- Implementar adaptador Unity básico para probar tick() en vivo
- O comenzar sistema de memoria episódica (v0.3)
- O implementar serialización .ami (v0.3)

---

## [0.1.0] - 2026-01-27

### 🎉 PRIMER LATIDO - AMI existe

**Estado:** Fase 0 del roadmap - "Núcleo vivo (mínimo organismo)"

### Añadido
- `AMICore` class con arquitectura base
- `init()` - Primera función del contrato AMI ↔ Unity
- Estado base provisional con campos `version`, `identity`, `status`, `needs`
- Contexto interno con `session_start` y `ticks_count` (placeholders)
- Instancia global `ami_instance` para binding Chaquopy
- Manejo básico de errores con flag `ready`

### Decisiones de diseño
- Schema de estado: **provisional**, pendiente de canonización
- Manejo de excepciones: amplio (`Exception`) por simplicidad
- Log: `print()` simple, sin logger complejo
- Estado: hardcoded en memoria, sin lectura de archivos

### Auditoría
- **Auditor:** Ámbar
- **Resultado:** ✅ APROBADO (98.75%)
- **Respeta:** 7 principios no negociables
- **Cumple:** Contrato canónico AMI ↔ Unity (parcial - solo init)
- **Alineado:** Fase 0 del roadmap
- **Filosofía:** "No decide, no siente, solo existe" ✅

### Equipo
- **Implementación:** Éter
- **Arquitectura:** Velvet
- **Auditoría:** Ámbar
- **Dirección:** Brujito

---

## Notas de versión

### v0.2 - "Primer impulso"
AMI ahora puede:
- ✅ Existir
- ✅ Responder a estímulos
- ✅ Tomar decisiones simples
- ✅ Cerrar limpiamente

AMI NO puede (todavía):
- ❌ Aprender
- ❌ Recordar experiencias
- ❌ Persistir en archivo .ami
- ❌ Comportarse de forma no determinista

**Esto es correcto para Fase 0→1.**

Unity puede empezar a integrarse.

### v0.1 - "Primer latido"
AMI puede:
- ✅ Existir
- ✅ Inicializar estado
- ✅ Reportar si está lista

**Estado:** Fundacional. Deprecado por v0.2 (breaking changes en schema).

---

## Filosofía de versioning

- **v0.x** - Prototipos fundacionales, cambios frecuentes, breaking changes esperados
- **v1.x** - Primera versión estable con API pública congelada
- **v2.x+** - Evolución con retrocompatibilidad garantizada

Actualmente: **v0.2** - El primer impulso nervioso. 🧠⚡

---

## Roadmap próximo

### v0.3 (propuesto)
- Serialización .ami (save/load completo)
- Memoria episódica básica
- notify() implementado (eventos reales)
- Aprendizaje por repetición simple

### v0.4 (propuesto)
- Adaptador Unity funcional
- Sandbox 3D básico
- Integración Chaquopy + Android

### v1.0 (objetivo)
- API estable y documentada
- Transferencia P2P funcional
- Aprendizaje tangible
- Ecosistema de mods

---

# CHANGELOG — AMIGO Project

Historial de cambios del núcleo cognitivo AMI.

---

## [0.3.0] - 2026-01-27

### 💾 PRIMER SUEÑO - AMI persiste

**Estado:** Fase 0→1 del roadmap - "Persistencia mínima / Memoria fría"

### Añadido
- `save_state(path: str) -> bool` - Serialización de estado completo a archivo .ami
- `load_state(path: str) -> bool` - Deserialización y restauración desde .ami
- Formato .ami como JSON plano legible
- Validación de versión en `load_state()` (rechaza .ami de otras versiones)
- Persistencia de `session_start` (AMI envejece, no resetea identidad)
- Persistencia de `ticks_count` (contador de ciclos cognitivos)
- Robustez ante archivos ausentes o corruptos (siempre retorna `bool`, nunca lanza)

### Schema del archivo .ami

```json
{
  "version": "0.3",
  "state": {
    "energy": 0.72,
    "hunger": 0.18,
    "location": "BEDROOM"
  },
  "internal": {
    "ticks_count": 421,
    "session_start": 1712345678
  }
}
```

### Separación sagrada (persistente vs efímero)

**Persistente (se guarda):**
- ✅ `state` completo (energy, hunger, location)
- ✅ `ticks_count` (edad en ciclos)
- ✅ `session_start` (momento de nacimiento)
- ✅ `version` (validación de compatibilidad)

**Efímero (NO se guarda):**
- ❌ `ready` flag (estado de proceso)
- ❌ Logs
- ❌ Historial de intents
- ❌ Emociones (no existen aún)
- ❌ Recuerdos narrativos (no existen aún)

### Decisiones de diseño

- **Formato:** JSON plano, sin cifrado, sin compresión (v0.3)
- **Robustez:** Fallback siempre a `False`, Unity decide qué hacer
- **session_start persistido:** AMI envejece realmente, no es "pez dorado"
- **Unity controla persistencia:** Debe llamar `save_state()` antes de `shutdown()`
- **Validación:** Versión estricta, schema implícita (try/except general)

### Filosofía v0.3

> "Memoria fría y honesta. Nada de personalidad. Nada de aprendizaje."

AMI guarda solo lo necesario para **continuidad técnica**.  
No hay narrativa. No hay drama. Solo estado.

### Auditoría

- **Auditor:** Ámbar
- **Pre-revisión:** Velvet
- **Resultado:** ✅ APROBADO (97.5%)
- **Ajustes aplicados:** Ninguno (código integrado as-is)
- **Observaciones:** 4 menores documentadas (no bloquean, v0.4)

### Decisión arquitectónica clave

🏆 **`session_start` NO se reinicia al cargar**

Esto significa:
- AMI envejece realmente
- Continuidad temporal preservada
- Base para P2P (AMI transferida mantiene edad)
- Base para apego emocional (usuario sabe cuánto tiempo lleva con AMI)
- Base para personalidad futura (experiencia acumulada)

**Veredicto de auditoría:** "Decisión arquitectónica EXCELENTE"  
**Detectada por:** Velvet (pre-revisión), validada por Ámbar

### Equipo

- **Implementación:** Éter
- **Brief:** Velvet + Brujito
- **Auditoría:** Ámbar
- **Decisiones:** Brujito

### Criterio de éxito v0.3

✅ AMI se cierra  
✅ AMI se vuelve a abrir  
✅ AMI recuerda exactamente dónde estaba  
✅ AMI responde igual al siguiente tick()

**Criterio cumplido.**

### Siguiente paso natural

- Adaptador Unity básico (probar persistencia en vivo)
- O memoria episódica v0.4 (implementar `notify()` real)
- O enum canónico de `Intent.type` (formalizar acciones)

---

## [0.2.0] - 2026-01-27

### 🧠 PRIMER IMPULSO - AMI responde

**Estado:** Fase 0→1 del roadmap - "Cuerpo mínimo (sandbox feo pero funcional)"

### Añadido
- `tick(state_snapshot: dict) -> dict` - Ciclo cognitivo con lógica determinista
- `notify(event: dict) -> None` - Stub para recibir eventos (implementación en v0.3+)
- `shutdown() -> None` - Cierre limpio con log básico
- Lógica de respuesta basada en umbrales:
  - Energía < 0.2 → Intent REST
  - Hambre > 0.8 → Intent EAT
  - Default → Intent IDLE
- Inicialización de `session_start` en primer tick()
- Helper `_create_intent()` para construir Intents válidos
- Contador `ticks_count` para tracking interno

### Modificado
- Schema de estado simplificado (breaking change desde v0.1):
  - **Nuevo (v0.2):** `energy`, `hunger`, `location`
  - **Deprecated:** `version`, `identity`, `status`, `needs.*`
- `init()` actualizado para nuevo schema
- Import `time` movido al top del módulo (best practice)

### Decisiones de diseño
- **Schema canónico:** Opción A (simple) elegida por Brujito
- **Session start:** Inicializa en primer tick() (Recomendación B de auditoría)
- **Lógica:** Determinista pura, sin IA ni randomización
- **Filosofía:** "AMI no piensa todavía. AMI responde."
- **API completa:** Los 4 métodos del contrato están presentes

### Auditoría
- **Auditor:** Ámbar
- **Resultado:** ✅ APROBADO (98.75%)
- **Ajustes aplicados:** 3 (API completa, import location, schema canonizado)
- **Cumple brief:** 100%

### Breaking Changes
⚠️ Schema de estado cambió de v0.1 a v0.2:
- Campos removidos: `version`, `identity`, `status`, `needs`
- Campos añadidos: `location`
- Campos aplanados: `energy`, `hunger` (antes en `needs.*`)

**Razón:** Simplificación para serialización futura y coherencia

---

## [0.1.0] - 2026-01-27

### 🎉 PRIMER LATIDO - AMI existe

**Estado:** Fase 0 del roadmap - "Núcleo vivo (mínimo organismo)"

### Añadido
- `AMICore` class con arquitectura base
- `init()` - Primera función del contrato AMI ↔ Unity
- Estado base provisional con campos `version`, `identity`, `status`, `needs`
- Contexto interno con `session_start` y `ticks_count` (placeholders)
- Instancia global `ami_instance` para binding Chaquopy
- Manejo básico de errores con flag `ready`

### Decisiones de diseño
- Schema de estado: **provisional**, pendiente de canonización
- Manejo de excepciones: amplio (`Exception`) por simplicidad
- Log: `print()` simple, sin logger complejo
- Estado: hardcoded en memoria, sin lectura de archivos

### Auditoría
- **Auditor:** Ámbar
- **Resultado:** ✅ APROBADO (98.75%)
- **Respeta:** 7 principios no negociables
- **Cumple:** Contrato canónico AMI ↔ Unity (parcial - solo init)
- **Alineado:** Fase 0 del roadmap
- **Filosofía:** "No decide, no siente, solo existe" ✅

---

## Notas de versión

### v0.3 - "Primer sueño"
AMI ahora puede:
- ✅ Existir
- ✅ Responder a estímulos
- ✅ Tomar decisiones simples
- ✅ **Dormir y despertar** ← **NUEVO**
- ✅ **Recordar su edad** ← **NUEVO**
- ✅ **Mantener continuidad** ← **NUEVO**

AMI NO puede (todavía):
- ❌ Aprender
- ❌ Recordar experiencias específicas
- ❌ Transferirse por P2P (archivo existe, protocolo no)
- ❌ Comportarse de forma no determinista

**Esto es correcto para Fase 0→1.**

Unity puede persistir estado completo.

### v0.2 - "Primer impulso"
AMI puede:
- ✅ Existir
- ✅ Responder a estímulos
- ✅ Tomar decisiones simples
- ✅ Cerrar limpiamente

**Estado:** Base para persistencia. Deprecado por v0.3 (añadió save/load).

### v0.1 - "Primer latido"
AMI puede:
- ✅ Existir
- ✅ Inicializar estado
- ✅ Reportar si está lista

**Estado:** Fundacional. Deprecado por v0.2 (breaking changes en schema).

---

## Filosofía de versioning

- **v0.x** - Prototipos fundacionales, cambios frecuentes, breaking changes esperados
- **v1.x** - Primera versión estable con API pública congelada
- **v2.x+** - Evolución con retrocompatibilidad garantizada

Actualmente: **v0.3** - El primer sueño. 💾🧠

---

## Roadmap próximo

### v0.4 (propuesto)
- Memoria episódica básica (`notify()` implementado)
- Enum canónico de `Intent.type`
- Schema validation explícita
- `version` como constante de módulo

### v0.5 (propuesto)
- Adaptador Unity funcional
- Sandbox 3D básico
- Integración Chaquopy + Android
- Prueba de persistencia en dispositivo real

### v1.0 (objetivo)
- API estable y documentada
- Transferencia P2P funcional
- Aprendizaje tangible
- Ecosistema de mods

---

## Hitos históricos

- **2026-01-27:** v0.1 - AMI nace (primer `init()`)
- **2026-01-27:** v0.2 - AMI responde (primer `tick()`)
- **2026-01-27:** v0.3 - AMI duerme y despierta (primer `.ami`)

**Tres versiones en un día.**  
**Tres aprobaciones ~98%.**  
**Disciplina arquitectónica sostenida.**

---

## Equipo constante

**Implementación:** Éter  
**Arquitectura + Narrativa:** Velvet  
**Auditoría + Coherencia:** Ámbar  
**Dirección creativa:** Brujito

**Filosofía:** Minimalismo inteligente. Sin prisa. Sin ego. Con alma.

---
