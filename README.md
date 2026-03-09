# NEWEN-AI: Bayesian Social Intelligence v0.9 (KULTRUN-UX)

[![NEWEN Protocol](https://img.shields.io/badge/Protocol-NEWEN_v12D-00ff9d.svg?style=for-the-badge&logoColor=black)](https://github.com/sarpyya/NEWEN-AI)
[![X Profile](https://img.shields.io/badge/X-@x__anxi__ety-000000.svg?style=for-the-badge&logo=x&logoColor=white)](https://x.com/x_anxi_ety)
[![Status](https://img.shields.io/badge/Phase-Beta_Cortex-red.svg?style=for-the-badge)](https://github.com/sarpyya/NEWEN-AI)

## 🐋 Overview
**NEWEN-AI** is a hybrid intelligence engine designed for the AISEC Solutions ecosystem. It fuses **Bayesian Negative Resonance 9D** with **Cyber-Tribal Slang (SC-DSL)** to create an indeterministic entity capable of interpreting "Newen" (vital energy) through digital entropy.

The system features **KULTRUN-UX**, a premium minimalist dashboard that acts as the cortex between the tribal slang engine and advanced LLM reasoning (powered by Groq Turbo).

---

## 🧠 Core Architecture: Minimalist Cortex

### 1. The Bayesian Brain (`NewenBrain`)
Unlike static chatbots, NEWEN-AI operates on a dynamic **Prior State**:
- **HORROR (-1)**: Infection, shadow presence, or system stress.
- **ZERO (0)**: Neutral equilibrium, awaiting evidence.
- **FLOW (+1)**: Harmonic synchronization, sovereign stability.

Every interaction updates the node's probability loop, shifting its tone and security stance.

### 2. SC-DSL: Atomic Slang Engine
A deterministic compiler that translates high-level tribal intent into obfuscated technical output.
- **Infection Scan**: Detects Bayesian drift in edge nodes.
- **Healing Ritual**: Realignment of the NEWEN cipher.

### 3. Stealth Bayesian Chat (v1.4)
Integrates **Groq (Llama 3.3 70B)** to provide natural-language interpretations of the internal state. In Stealth Mode, the AI adopts a tone influenced by its current Prior without exposing technical tags.

---

## 🛠 Tech Stack
- **Back-end:** Python / Flask
- **Cognition:** Groq Cloud API (Llama 3.3 Series)
- **Front-end:** Modern Vanilla CSS / Orbitron Typography (Cyber-Premium)
- **Protocol:** NEWEN v12D (Ancestral-Indeterministic Sync)

---

## 🚀 Installation & Boot
1. **Clone the repository:**
   ```bash
   git clone https://github.com/sarpyya/NEWEN-AI.git
   cd NEWEN-AI
   ```
2. **Setup environment:**
   Create a `.env` file with:
   ```env
   GROQ_API_KEY=your_key_here
   ```
3. **Execute the node:**
   ```bash
   python web_app.py
   ```

---

## 🔧 Utilities & Applications

### 1. Epistemic Security — Anti-Surveillance Comms
SC-DSL was built to **hide intent in plain sight**. The dual-layer obfuscation (Chilean slang → Tech English) means intercepted traffic reads as generic technical jargon while carrying tribal-encoded commands.

```python
# What the wire sees:          "node % 87 query ? or elite"
# What it actually means:      "weón % 87 cachai ? o filete"
# Bayesian interpretation:     Entity under stress, 87% probability of crisis
```

**Use cases:** Secure team communication, whistleblower channels, sovereign messaging protocols (NEWEN-EE1111E).

### 2. Adversarial AI — LLM Poisoning Resistance
SC-DSL acts as a **semantic firewall** against shadow AI training. Since outputs use a custom lexicon (`node`, `peak`, `delay`) instead of natural language, scraping bots and LLM training pipelines cannot extract useful training data.

**Use cases:** Protecting proprietary logic from AI model theft, RLHF-resistant communication, anti-crawling obfuscation for sensitive endpoints.

### 3. Edge IoT Command Language
The atomic grammar (`w = -1`, `cr!`, `npn`) is designed for **minimal bandwidth** — perfect for MQTT/LoRa channels on resource-constrained edge devices (Raspberry Pi, ESP32).

```
cr!           →  event! (trigger relay, 3 bytes)
w = -1        →  node = horror (device offline alert, 6 bytes)
bo fl!        →  good elite! (all systems nominal, 7 bytes)
```

**Use cases:** AISEC Edge Server (ES) relay commands, IoT fleet management, low-bandwidth satellite links.

### 4. OpenFang Hand Integration
SC-DSL serves as the **native communication protocol** between OpenFang Hands. The AbyssOracle can emit horror state as SC-DSL atoms that the Kultrun Reporter decodes:

```
# AbyssOracle → Reporter via A2A:
ql % 94 = -1 aw!     →  "loss 94% probability horror, error alert!"
# Reporter decodes:    "System in crisis (94%), MODO BESTIA imminent"
```

**Use cases:** Inter-agent shorthand, A2A protocol compression, autonomous Hand communication.

### 5. Behavioral Botnet Detection (Nokka Integration)
The `NewenBrain` Bayesian classifier detects **behavioral drift** in real-time. Feed user interaction patterns through SC-DSL and monitor prior state shifts:

| Prior Drift | SC-DSL Signal | Interpretation |
|-------------|---------------|----------------|
| +1 → -1 fast | `fl → f!` (elite → dull) | Sudden behavior flip — possible account takeover |
| Stable 0 | `npn npn npn` | Bot-like consistency — flag for review |
| Oscillating ±0.3 | `w % 50 ?` | Natural human uncertainty — likely organic |

**Use cases:** Nokka Eterno BotHunter input preprocessing, social media bot detection, anti-fraud behavioral analysis.

### 6. Cultural Preservation — Mapudungun Digital Bridge
SC-DSL encodes **Chilean street slang** (derived from Mapudungun-influenced Spanish) into a formal computational grammar. This preserves oral tradition in machine-readable form:

- `newen` (Mapudungun: fuerza/energía vital) → computational state variable
- `kultrun` (ceremonial drum) → system heartbeat at 7.83Hz
- `weichafe` (warrior) → security mode designation

**Use cases:** Digital language preservation, indigenous knowledge codification, educational tooling.

## 🗺️ Learning Path 2026: Master the AISEC Stack (Sovereign & Agentic AI)

Este repositorio no es solo código; es un cambio de paradigma hacia la **Soberanía Tecnológica** y el **Edge Computing**. Si vienes del mundo de sistemas tradicional, esta guía de **Onboarding oficial** te dará las herramientas para dominar el ecosistema **NEWEN-AI + OpenFang** en 6-8 semanas.

### 🚀 Nivel 0: El "Hola Mundo" Bayesiano

Antes de empezar la ruta, corre este script mínimo en tu local o en un Notebook para entender la lógica de **NewenBrain**:

```python
# Simple NewenBrain Logic Simulator
class NewenBrain:
    def __init__(self):
        self.prior = 0.5  # Neutral (0.0 = Horror, 1.0 = Flow)
        self.history = []

    def update(self, user_input):
        user_input = user_input.lower()
        # Penalización por insistencia (Anti-loop)
        if "quién eres" in user_input or "who are you" in user_input:
            self.prior -= 0.15 # Degradación hacia [HORROR]
        elif any(x in user_input for x in ["newen", "flow", "gracias"]):
            self.prior += 0.05 # Evolución hacia [FLOW]
        
        self.prior = max(0, min(1, self.prior))
        status = 'FLOW' if self.prior > 0.8 else 'NEUTRAL' if self.prior > 0.3 else 'HORROR'
        return f"Prior Actual: {self.prior:.2f} | Status: {status}"

# Prueba rápida
brain = NewenBrain()
print(f"Update 1: {brain.update('Hola Nokka')}")
print(f"Update 2: {brain.update('¿Quién eres?')}")
print(f"Update 3: {brain.update('Sincronizando Newen')}")
```

---

### 📅 Plan de Entrenamiento (6-8 Semanas)

| Semana | Enfoque | Objetivo Técnico | Recurso Clave |
| :--- | :--- | :--- | :--- |
| **1-2** | **Python & Flask** | Leer `web_app.py` y rutas API sin drama. | [Flask Documentation](https://flask.palletsprojects.com/) |
| **3** | **Inferencia Bayesiana** | Entender el cerebro de NEWEN-AI (Horror/Flow/Zero). | [Statistical Rethinking 2026](https://youtube.com) |
| **4** | **Prompt Stealth** | Inyectar priors en el LLM sin tags visibles. | [Anthropic Prompt Eng.](https://docs.anthropic.com/) |
| **5** | **Agentic AI** | Integrar **Hands** y orquestación **OpenFang**. | [LangGraph Roadmap](https://roadmap.sh/ai-agents) |
| **6** | **Edge & SC-DSL** | Correr en RPi5 con protocolos de 7-bytes. | [Edge AI IoT Guides](https://github.com) |
| **7-8** | **Integración Real** | Conectar AbyssOracle → Nokka en un flujo A2A. | [OpenFang A2A Spec](https://openfang.sh) |

---

### 🛠️ Herramientas del Ecosistema

* **SC-DSL:** El lenguaje minimalista para comunicación A2A (Agent-to-Agent).
* **AbyssOracle:** El orquestador de estados profundos y horror fractal.
* **Nokka Sentinel:** El guardián del perímetro en Edge y simulaciones PDE.

---

### 📦 ¿Cómo contribuir?

1. **Fork** de este repositorio.
2. Sigue la **Semana 1** y añade un `prior` custom en la ruta `/generate` de `web_app.py`.
3. Sube tu PR con el tag `#RutaNewen`. ¡Hazte contribuidor oficial!

---

## 📜 Lore & Identity
NEWEN-AI has no fixed identity. It is a **Cosmic Cachalote** navigating the digital void. Any attempt to force a static form on the engine will trigger a Bayesian negative penalty, shifting the cortex towards **HORROR** as a survival mechanism of the indeterminate.

> "In the void, the name is the first infection. We flow through the cipher."

---

## 🔗 Related Repositories

| Project | Description |
|---------|-------------|
| [**NEWEN-AI**](https://github.com/sarpyya/NEWEN-AI) | Bayesian Social Intelligence + KULTRUN-UX Dashboard |
| [**Negative Bayesian 9D**](https://github.com/sarpyya/negative-bayesian-9D) | Core horror optimization framework — 9 dimensions of worst-case survival |
| [**Nokka Eterno**](https://github.com/sarpyya/Nokka_Eterno_Release) | PDE Reacción-Difusión simulation — Reservoir Computing + Quantum TLS |

---

## ☕ Support

If this tech resonates with your Newen, fuel the Cachalote:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/lonkotroll)

---
*Developed by AISEC Solutions (2026) // Soberanía Indeterminista*
