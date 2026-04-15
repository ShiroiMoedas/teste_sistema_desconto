def calcular_desconto():
    print("=== SISTEMA DE DESCONTOS v1.0 (QA TEST) ===")
    valor_compra = 100
    percentual = 10
    try:
        if valor_compra <= 0:
            print("❌ O valor da compra deve ser positivo.")
            return

        percentual = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))

        if percentual < 0 or percentual > 50:
            print("❌ O desconto deve estar entre 0% e 50%.")
            return

        desconto = valor_compra * (percentual / 100)
        valor_final = valor_compra - desconto

        print("\n✅ Processado com sucesso!")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Valor Final: R$ {valor_final:.2f}")

    except ValueError:
        print("❌ Erro: Digite apenas números válidos.")

if __name__ == "__main__":
    calcular_desconto()