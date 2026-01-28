# ami_core.py - v0.3 - Persistencia mínima (.ami)
# AUDITORÍA PENDIENTE: Ámbar

import time
import json
import os

class AMICore:
    """
    Núcleo cognitivo de AMI.
    Responsabilidades v0.3:
    - Persistencia de estado canónico (Save/Load)
    - Continuidad de sesión (ticks_count, session_start)
    - Robustez ante archivos corruptos o ausentes
    """
    
    def __init__(self):
        self.ready = False
        self.state = {
            "energy": 1.0,
            "hunger": 0.0,
            "location": "UNKNOWN"
        }
        self._internal_context = {
            "session_start": None,
            "ticks_count": 0,
            "version": "0.3"
        }

    def init(self) -> bool:
        """Inicializa el entorno básico (ahora preparando el terreno para load_state)."""
        try:
            self._internal_context["session_start"] = None # Espera al primer tick o load
            self._internal_context["ticks_count"] = 0
            self.ready = True
            print("AMI core initialized")
            return True
        except Exception:
            self.ready = False
            return False

    # --- PERSISTENCIA (v0.3) ---

    def save_state(self, path: str) -> bool:
        """Serializa el estado actual y contexto interno en un archivo .ami (JSON)."""
        try:
            payload = {
                "version": self._internal_context["version"],
                "state": self.state,
                "internal": {
                    "ticks_count": self._internal_context["ticks_count"],
                    "session_start": self._internal_context["session_start"]
                }
            }
            
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(payload, f, indent=4)
            
            return True
        except Exception:
            return False

    def load_state(self, path: str) -> bool:
        """Carga y valida un archivo .ami. Si algo falla, mantiene el estado actual y retorna False."""
        if not os.path.exists(path):
            return False
            
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Validación de versión (Regla v0.3)
            if data.get("version") != self._internal_context["version"]:
                return False
                
            # Carga de datos
            self.state.update(data["state"])
            self._internal_context["ticks_count"] = data["internal"]["ticks_count"]
            self._internal_context["session_start"] = data["internal"]["session_start"]
            
            return True
        except Exception:
            return False

    # --- CICLO DE VIDA ---

    def tick(self, state_snapshot: dict) -> dict:
        if not self.ready: return self._create_intent("IDLE", "SAFE", 0.0)
        
        # Iniciar sesión si es nueva o no cargada
        if self._internal_context["session_start"] is None:
            self._internal_context["session_start"] = time.time()

        self.state.update(state_snapshot)
        self._internal_context["ticks_count"] += 1

        # Lógica v0.2 conservada
        if self.state.get("energy", 1.0) < 0.2:
            return self._create_intent("REST", "BED", urgency=0.9)
        if self.state.get("hunger", 0.0) > 0.8:
            return self._create_intent("EAT", "KITCHEN", urgency=0.7)

        return self._create_intent("IDLE", "CURRENT", urgency=0.1)

    def notify(self, event: dict) -> None:
        """Stub para eventos futuros (v0.4+)."""
        pass

    def shutdown(self) -> None:
        """Cierre limpio. (Nota: Unity debe llamar a save_state antes o aquí)."""
        self.ready = False
        print("AMI core shutdown")

    def _create_intent(self, action_type: str, target: str, urgency: float) -> dict:
        return {
            "type": action_type,
            "target": target,
            "style": "DEFAULT",
            "urgency": urgency
        }

# Instancia global
ami_instance = AMICore()
