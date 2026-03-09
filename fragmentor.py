import os
import argparse
import random

def fragment_system(source_dir, level):
    """
    Simula la fragmentación del sistema para el protocolo FACT.
    Nivel 0: Completo
    Nivel 1: Sin comentarios
    Nivel 2: Solo signaturas (sin cuerpos)
    Nivel 3: Solo nombres de archivos y propósitos
    Nivel 4: Fragmentos aislados (muestreo aleatorio de líneas)
    """
    print(f"--- FACT PROTOCOL: Fragmentación Nivel {level} ---")
    
    files = [f for f in os.listdir(source_dir) if f.endswith('.py') or f.endswith('.md')]
    
    for filename in files:
        filepath = os.path.join(source_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        print(f"\n[FILE: {filename}]")
        
        if level == 0:
            print(content)
        elif level == 1:
            # Eliminar comentarios de python básicos (muy simplificado)
            import re
            content = re.sub(r'#.*', '', content)
            print(content)
        elif level == 2:
            # Solo def y class (Python)
            for line in content.split('\n'):
                if line.strip().startswith(('def ', 'class ', 'import ', 'from ')):
                    print(line)
        elif level == 3:
            # Solo primer párrafo o resumen
            lines = content.split('\n')
            print(lines[0] if lines else "Empty file")
        elif level == 4:
            # Muestreo aleatorio (10%)
            lines = content.split('\n')
            sample = random.sample(lines, max(1, len(lines) // 10))
            print("... [FRAGMENTED DATA] ...")
            print('\n'.join(sample))
            print("... [FRAGMENTED DATA] ...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FACT Fragmentor Utility")
    parser.add_argument("--dir", default=".", help="Directorio a fragmentar")
    parser.add_argument("--level", type=int, default=1, choices=[0, 1, 2, 3, 4], help="Nivel de fragmentación")
    args = parser.parse_args()
    
    fragment_system(args.dir, args.level)
