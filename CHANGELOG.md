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
