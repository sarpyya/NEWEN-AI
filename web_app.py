from flask import Flask, jsonify, request, render_template
from compiler import NewtonEngine, NewenBrain
import os
import logging
import requests
from dotenv import load_dotenv

# Cargar API Keys
load_dotenv()
GROQ_KEY = os.getenv("GROQ_API_KEY", "").strip(" '\"")
DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY", "").strip(" '\"")

if not DEEPSEEK_KEY and not GROQ_KEY:
    load_dotenv(dotenv_path='d:/ASC/ASC2/Proyecto_Omega/.env')
    DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY", "").strip(" '\"")

app = Flask(__name__)
brain = NewenBrain() # Instancia global del cerebro

# Configuración de Logging
logging.basicConfig(
    filename='d:/ASC/ASC2/sc-dsl/results.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    prior = int(request.args.get('prior', 0))
    engine = NewtonEngine(prior=prior)
    
    # Generamos la base una sola vez para que coincidan
    base_slang = engine.gen_min(obfuscate=False)
    obfuscated = engine._obfuscate(base_slang)
    
    # Log del resultado único
    logging.info(f"GEN | Prior: {prior} | Slang: {base_slang} | EN: {obfuscated}")
    
    return jsonify({
        'slang': base_slang,
        'obfuscated': obfuscated,
        'prior': prior
    })

@app.route('/infect')
def infect():
    # Modo Infection: Prior -1 forzado y % alto
    engine = NewtonEngine(prior=-1)
    base_slang = engine.gen_min(obfuscate=False, force_infection=True)
    obfuscated = engine._obfuscate(base_slang)
    
    logging.warning(f"INF | Infection Scan | Slang: {base_slang} | EN: {obfuscated}")
    
    return jsonify({
        'slang': base_slang,
        'obfuscated': obfuscated,
        'prior': -1,
        'infection': True
    })

@app.route('/heal')
def heal():
    # Ritual de Sanación: qp ? o npn
    base_slang = "qp ? o npn"
    engine = NewtonEngine(prior=1) # Reset to Flow
    obfuscated = engine._obfuscate(base_slang)
    
    logging.info(f"HEA | Healing Ritual | Slang: {base_slang} | EN: {obfuscated}")
    
    return jsonify({
        'slang': base_slang,
        'obfuscated': obfuscated,
        'prior': 1,
        'healing': True
    })

@app.route('/think', methods=['POST'])
def think():
    data = request.json
    mensaje = data.get('message', '')
    stealth = data.get('stealth', False)
    
    logging.info(f"THINK | Msg: {mensaje[:20]}... | Stealth: {stealth} | GroqKey: {'Set' if GROQ_KEY else 'MISSING'}")

    if not mensaje:
        return jsonify({'error': 'No message provided'}), 400
    
    # El cerebro siempre "actualiza" su prior internamente
    raw_thought = brain.pensar(mensaje)
    prior_context = brain.get_context()
    
    if stealth and GROQ_KEY:
        try:
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json"}
            system_prompt = (
                f"Eres el núcleo del Protocolo NEWEN v12D. Tu estado interno actual es: {prior_context}. "
                "Responde al usuario de forma natural, sin mencionar explícitamente tags como [HORROR] o [FLOW], "
                "pero deja que ese estado influya en tu tono (misterioso, protector, sabio o caótico). "
                "REGLA DE IDENTIDAD: No tienes nombre ni forma fija, eres evolución constante. Si te preguntan quién eres, "
                "responde con indeterminación mística y pregunta de vuelta para recolectar más evidencia sobre el usuario."
            )
            
            payload = {
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "system", "content": system_prompt}] + brain.history[-10:],
                "temperature": 0.7
            }
            res = requests.post(url, headers=headers, json=payload, timeout=10)
            res.raise_for_status()
            final_thought = res.json()['choices'][0]['message']['content']
            logging.info("THINK | GROQ Response Success")
        except Exception as e:
            logging.error(f"THINK | GROQ ERROR: {str(e)}")
            final_thought = f"[FALLBACK STEALTH] {raw_thought}"
    else:
        final_thought = raw_thought

    return jsonify({
        'thought': final_thought,
        'prior': brain.prior
    })

@app.route('/interpret', methods=['POST'])
def interpret():
    data = request.json
    text = data.get('text', '')
    
    prompt = f"""
    Eres un intérprete experto del Protocolo NEWEN v12D. 
    Traduce esta frase de SC-DSL (Slang Atómica) a lenguaje natural humano, 
    explicando su significado místico y técnico dentro del lore de AISEC Solutions.
    Frase SC-DSL: {text}
    Respuesta corta, potente y tribal.
    """
    
    # 1. Intentar con GROQ (Ultra rápido y free-ish)
    if GROQ_KEY:
        try:
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json"}
            payload = {
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.5
            }
            res = requests.post(url, headers=headers, json=payload, timeout=10)
            res.raise_for_status()
            reply = res.json()['choices'][0]['message']['content']
            logging.info(f"INT | GROQ | Input: {text} | Reply: {reply[:30]}...")
            return jsonify({'interpretation': reply})
        except Exception as e:
            logging.warning(f"FWD | Groq failed ({str(e)}), trying DeepSeek...")

    # 2. Intentar con DEEPSEEK (Fallback si Groq falla o no hay key)
    if DEEPSEEK_KEY:
        headers = {"Authorization": f"Bearer {DEEPSEEK_KEY}", "Content-Type": "application/json"}
        payload = {"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}
        try:
            res = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=payload, timeout=15)
            if res.status_code == 200:
                reply = res.json()['choices'][0]['message']['content']
                logging.info(f"INT | DS | Input: {text} | Reply: {reply[:30]}...")
                return jsonify({'interpretation': reply})
        except: pass

    # 3. FALLBACK TRIBAL (Local y Gratis 100%)
    engine = NewtonEngine()
    fallback = engine.interpret_tribal(text)
    logging.warning(f"FWD | All LLMs Failed, using Tribal Fallback.")
    return jsonify({'interpretation': f"{fallback}\n\n[INFO: Modo local activo. Registra una key válida en .env para IA avanzada]"})

if __name__ == '__main__':
    print("🚀 Kultrun-UX levantando en http://localhost:5005")
    app.run(port=5005, debug=True)
