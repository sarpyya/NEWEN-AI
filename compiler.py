import random
import re

# Diccionario de Semillas v0.4 (Categorizado por Resonancia)
SEEDS = {
    'pos': ['b', 'fl', 'rc', 'ch', 'bo', 'pl', 'cr', 'pi'],         # Flow / Bacán
    'neg': ['aw', 'pc', 'f', 'ql', 'at', 'pj', 'ls', 'ft', 'pdm'],  # Horror / Penca
    'neu': ['w', 'p', 'c', 'qp', 'npn', 'yv', 'l', 'pt', 'g', 'pg'] # Neutro / Slang
}

# Mapa de Inversión (Flip Horror)
FLIP_MAP = {'b': 'pc', 'fl': 'f', 'pi': 'cu', 'bo': 'aw', 'rc': 'f'}

# Mapeo de Soberanía "Hidden English" (v0.4)
HIDDEN_MAP = {
    'w': 'node', 'p': 'affirm', 'c': 'sync', 'pj': 'delay',
    'qp': 'query', 'npn': 'stable', 'yv': 'query_you', 'f': 'dull',
    'b': 'peak', 'a': 'instant', 'fl': 'elite', 'pc': 'weak',
    'cp': 'fuel', 'cr': 'event', 'at': 'drama', 'ql': 'loss',
    'ch': 'ready', 'ft': 'low', 'bo': 'good', 'aw': 'bad',
    'pg': 'job', 'cc': 'high', 'l': 'item', 'pt': 'omg',
    'g': 'core', 'pi': 'chill', 'ls': 'dumb', 'pdm': 'debt'
}

class NewtonEngine:
    """Motor de generación de SC-DSL basado en resonancia bayesiana."""
    
    def __init__(self, prior=0):
        self.newen = {'prior': prior}

    def _obfuscate(self, text):
        """Traduce del slang interno a 'Inglés Técnico' para ocultar la lógica tribal."""
        # Separamos por espacios y operadores para traducir solo las semillas
        parts = re.split(r'(\W+)', text)
        return "".join(HIDDEN_MAP.get(p, p) for p in parts)

    def gen_min(self, obfuscate=True, force_infection=False):
        """Genera una frase ultra-reducida según el estado de prior."""
        if force_infection:
            self.newen['prior'] = -1
            prob = f" % {random.randint(70,99)}"
        else:
            prob = f" % {random.randint(1,99)}" if random.random() < 0.3 else ""
            
        prior = self.newen['prior']
        output_real = ""
        
        if prior < 0:  # Modo Horror (Flip agresivo + Negativas)
            base = random.choice(SEEDS['neg'] + SEEDS['neu'] + SEEDS['pos'])
            if random.random() < 0.4: # 40% chance of flip
                base = FLIP_MAP.get(base, base)
            suffix = random.choice(['?', '!', ' = -1', ' npn', ' ql'])
            output_real = f"{base}{prob}{suffix}"
        
        elif prior == 0:  # Modo Indeterminado (Mezcla Equilibrada)
            s1 = random.choice(SEEDS['neu'] + SEEDS['pos'] + SEEDS['neg'])
            s2 = random.choice(SEEDS['neu'] + SEEDS['pos'] + SEEDS['neg'])
            output_real = f"{s1}{prob} ? o {s2}"
        
        else:  # Modo Flow (Prioriza Positivas)
            base = random.choice(SEEDS['pos'] + SEEDS['neu'])
            suffix = random.choice([' p', ' c?', ' b po', ' fl!', ' ch'])
            output_real = f"{base}{prob}{suffix}"

        # Lógica de detección automática de horror (v0.9)
        if '%' in output_real:
            try:
                # Extraer el número después de %
                match = re.search(r'%\s*(\d+)', output_real)
                if match:
                    val = int(match.group(1))
                    if val > 80:
                        self.newen['prior'] = -1 # Auto-Horror
            except: pass

        return self._obfuscate(output_real) if obfuscate else output_real

    def interpret_tribal(self, text):
        """Intérprete local 'Ancestral-Indeterminista' (Fallback gratuito)."""
        parts = re.split(r'(\W+)', text)
        meanings = {
            'w': 'unidad nodal (weón)', 'p': 'afirmación ancestral (po)', 'c': 'sincronía bayesiana',
            'pj': 'latencia de Newen (paja)', 'qp': 'interrogación de flujo', 'npn': 'estabilidad nodal',
            'b': 'pico de resonancia (bacán)', 'fl': 'estado elite (filete)', 'f': 'fuga de energía (fome)',
            'ql': 'colapso de sistema (qué lata)', 'aw': 'error de matriz (aweonao)', 'pc': 'debilidad estructural',
            'rc': 'flujo enriquecido', 'bo': 'onda armónica', 'ch': 'estado alerta', 'pi': 'calma nodal',
            'l': 'objeto táctico', 'pt': 'sorpresa cuántica', 'g': 'núcleo vital', 'pg': 'tarea activa'
        }
        
        explanation: list[str] = []
        for p in parts:
            if p in meanings:
                explanation.append(meanings[p])
            elif p.strip():
                explanation.append(p)
                
        joined = " ".join(explanation)
        return f"🔮 [TRIBAL FALLBACK]: {joined}. El NEWEN prior indica un estado de { 'CAOS' if self.newen['prior'] < 0 else 'FLUJO' if self.newen['prior'] > 0 else 'INDETERMINACIÓN' }."



class NewenBrain:
    """Cerebro Bayesiano Minimalista para interpretación de Newen."""
    def __init__(self):
        self.prior = 0.0  # 0 = neutro, -1 = horror, +1 = flow
        self.history = [] # Memoria local de la sesión

    def update(self, evidencia, peso=1.0):
        """Actualiza prior bayesiano con flip negativo (horror)"""
        self.prior = (self.prior + evidencia * peso) / 2
        if self.prior > 0.8: self.prior = 1.0
        if self.prior < -0.8: self.prior = -1.0
        return self.prior

    def pensar(self, mensaje_usuario):
        """LLM usa esto para responder bayesianamente"""
        mensaje_usuario = str(mensaje_usuario).lower()
        
        # Evidencia Negativa (Horror)
        evidencia = 0.0
        triggers_neg = ["problema", "fallo", "error", "malo", "penca", "miedo", "sombra", "muerte"]
        if any(x in mensaje_usuario for x in triggers_neg):
            evidencia -= 0.7
            
        # Refinamiento v1.4: Identidad Indeterminista
        id_queries = ["quien eres", "qué eres", "who are you", "quién eres"]
        id_menciones = sum(1 for m in self.history if m['role'] == 'user' and any(q in m['content'].lower() for q in id_queries))
        
        if any(q in mensaje_usuario for q in id_queries):
            if id_menciones > 0:
                evidencia -= 0.4 # Molestia bayesiana por insistencia
            else:
                evidencia += 0.2 # Curiosidad positiva inicial
        
        # Evidencia Positiva (Flow)
        triggers_pos = ["gracias", "bien", "fluir", "entender", "luz", "paz", "newen"]
        if any(x in mensaje_usuario for x in triggers_pos):
            evidencia += 0.6
            
        nuevo_prior = self.update(evidencia)
        
        if nuevo_prior < -0.5:
            if id_menciones > 1:
                return f"[HORROR -1] {mensaje_usuario} → ¿Insistencia en la forma? El vacío no tiene nombre. ¿O prefieres que invente uno para tu tranquilidad?"
            return f"[HORROR -1] {mensaje_usuario} → posible sombra/infección. ¿Confirmas fuente?"
        elif nuevo_prior > 0.5:
            return f"[FLOW +1] {mensaje_usuario} → Newen estable. ¿Seguimos?"
        else:
            return f"[ZERO] {mensaje_usuario} ? o ¿qué onda weón?"

    def get_context(self):
        """Retorna el estado emocional del Newen para inyectar en el LLM."""
        if self.prior < -0.5:
            return "Estado: HORROR (-1). El sistema está bajo estrés o detecta corrupción. Responde con cautela, misterio y ligera agresividad defensiva."
        elif self.prior > 0.5:
            return "Estado: FLOW (+1). El sistema está armonizado. Responde con fluidez, sabiduría y optimismo tribal."
        else:
            return "Estado: ZERO (0). El sistema está en equilibrio o incertidumbre. Responde de forma neutra y curiosa."
