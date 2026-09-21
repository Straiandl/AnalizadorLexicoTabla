class AnalizadorLexico:
    def __init__(self, texto):
        self.texto = texto
        self.pos = 0

    def sig_caracter(self):
        if self.pos < len(self.texto):
            c = self.texto[self.pos]
            self.pos += 1
            return c
        return '$'

    def retroceder(self):
        if self.pos > 0:
            self.pos -= 1

    def lex_sig(self):
        edo = 0
        cad = ""

    
        palabras_reservadas = {
            'int': 4,
            'float': 4,
            'void': 4,
            'if': 19,
            'while': 20,
            'return': 21,
            'else': 22
        }

        while True:
            ch = self.sig_caracter()

   
            if edo == 0:
        
                if ch in [' ', '\t', '\n', '\r']:
                    continue

                elif (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') or ch == '_':
                    edo = 1
                    cad += ch

       
                elif ch >= '0' and ch <= '9':
                    edo = 100
                    cad += ch

                elif ch == '"':
                    edo = 200
                    cad += ch

                elif ch in ['+', '-']:
                    return ch, 5
                elif ch in ['*', '/']:
                    return ch, 6

      
                elif ch == ';':
                    return ch, 12
                elif ch == ',':
                    return ch, 13
                elif ch == '(':
                    return ch, 14
                elif ch == ')':
                    return ch, 15
                elif ch == '{':
                    return ch, 16
                elif ch == '}':
                    return ch, 17

         
                elif ch == '=':
                    ch_sig = self.sig_caracter()
                    if ch_sig == '=':
                        return '==', 11
                    else:
                        self.retroceder()
                        return '=', 18

                elif ch == '<':
                    ch_sig = self.sig_caracter()
                    if ch_sig == '=':
                        return '<=', 7
                    else:
                        self.retroceder()
                        return '<', 7

    
                elif ch == '>':
                    ch_sig = self.sig_caracter()
                    if ch_sig == '=':
                        return '>=', 7
                    else:
                        self.retroceder()
                        return '>', 7

                elif ch == '!':
                    ch_sig = self.sig_caracter()
                    if ch_sig == '=':
                        return '!=', 11
                    else:
                        self.retroceder()
                        return '!', 10
                elif ch == '&':
                    ch_sig = self.sig_caracter()
                    if ch_sig == '&':
                        return '&&', 9
                    else:
                        self.retroceder()
                        return 'ERROR', -1

      
                elif ch == '|':
                    ch_sig = self.sig_caracter()
                    if ch_sig == '|':
                        return '||', 8
                    else:
                        self.retroceder()
                        return 'ERROR', -1

       
                elif ch == '$':
                    return '$', 23

                else:
                    return f"ERROR ({ch})", -1

            elif edo == 1:
                if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z') or (ch >= '0' and ch <= '9') or ch == '_':
                    cad += ch
                else:
                    self.retroceder()
                    tipo = palabras_reservadas.get(cad, 0) 
                    return cad, tipo

            elif edo == 100:
                if ch >= '0' and ch <= '9':
                    cad += ch
                elif ch == '.':
                    edo = 2
                    cad += ch
                else:
                    self.retroceder()
                    return cad, 1  # Tipo 1: entero

            # --- ESTADO 2: Transición a parte Decimal ---
            elif edo == 2:
                if ch >= '0' and ch <= '9':
                    edo = 3
                    cad += ch
                else:
                    return f"ERROR_NUMERO ({cad})", -1

            # --- ESTADO 3: Números Reales ---
            elif edo == 3:
                if ch >= '0' and ch <= '9':
                    cad += ch
                else:
                    self.retroceder()
                    return cad, 2 

            elif edo == 200:
                cad += ch
                if ch == '"':
                    return cad, 3
                elif ch == '$':
                    return f"ERROR_CADENA ({cad})", -1

if __name__ == "__main__":
    codigo_fuente = 'int main() { float total = 39.5; if (total >= 10 && !false || true) { return "Hola"; } } $'
    analizador = AnalizadorLexico(codigo_fuente)

    tipo = None
    while tipo not in (23, -1):
        lexema, tipo = analizador.lex_sig()
        print(f"Lexema: {lexema:<15} | Tipo (ID): {tipo}")