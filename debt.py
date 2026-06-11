def calcular_deuda_patrimonio():
    print("--- Calculadora de Ratio Deuda/Patrimonio ---")
    try:
        pasivo_total = float(input("Ingresa el Pasivo Total de la empresa: "))
        patrimonio_neto = float(input("Ingresa el Patrimonio Neto: "))

        if patrimonio_neto == 0:
            print("Error: El Patrimonio Neto no puede ser cero.")
            return

        ratio = pasivo_total / patrimonio_neto

        print(f"\nEl ratio Deuda/Patrimonio es: {ratio:.2f}")

        # Interpretación simple
        if ratio < 0.5:
            print("Interpretación: Bajo (Empresa conservadora, bajo riesgo financiero).")
        elif 0.5 <= ratio <= 1.5:
            print("Interpretación: Moderado (Estructura de capital equilibrada).")
        else:
            print("Interpretación: Alto (Empresa agresiva, alto riesgo financiero).")

    except ValueError:
        print("Error: Por favor, ingresa números válidos.")

if __name__ == "__main__":
    calcular_deuda_patrimonio()