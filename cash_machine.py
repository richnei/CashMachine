class CashMachine:
    def __init__(self):
        self.notes = {10: 0, 20: 0, 50: 0, 100: 0}

        # Add novas notas no caixa e verifica se o valor é aceito
    def refill_notes(self, note_value, quantity):
        if note_value in self.notes:
            self.notes[note_value] += quantity
            print(f"{quantity} notas de R$ {note_value:.2f} foram adicionadas.")
        else:
            print(f"O valor de nota R$ {note_value:.2f} não é aceito pelo caixa eletrônico.")

        # Verifica se é possivel sacar a quantia solicitada.
    def approve_withdrawal(self, value):
        if value > sum(k * v for k, v in self.notes.items()):
            print(f"Não é possível aprovar o saque de R$ {value:.2f}. Não há dinheiro suficiente na máquina.")
            return False
        else:
            return True
        
        #Libera as notas para realizar o saque. Se for possivel efetuar o saque, retorna uma lista com as notas liberadas
    def release_notes(self, value):
        notes_released = []
        for note_value in sorted(self.notes.keys(), reverse=True):
            while self.notes[note_value] > 0 and value >= note_value:
                value -= note_value
                self.notes[note_value] -= 1
                notes_released.append(note_value) 
        if value == 0:
            print(f"Saque aprovado. Notas liberadas: {notes_released}")
            return notes_released
        else:
            print(f"Não é possível concluir o saque de R$ {value:.2f} com as notas disponíveis.")
            return None

    

cm = CashMachine()

# Encher a máquina com notas

cm.refill_notes(10, 10)
cm.refill_notes(20, 10)
cm.refill_notes(50, 10)
cm.refill_notes(100, 10)

# Loop principal para interagir com o usuário

while True:
    print("O que você gostaria de fazer?")
    print("1 - Recarregar notas")
    print("2 - Sacar dinheiro")
    print("3 - Sair")
    
    choice = int(input("Digite sua escolha: "))

    if choice == 1:
        note_value = int(input("Digite o valor da nota: "))
        quantity = int(input("Digite a quantidade de notas: "))
        cm.refill_notes(note_value, quantity)
    elif choice == 2:
        value = int(input("Digite o valor a ser sacado: "))
        if cm.approve_withdrawal(value):
            cm.release_notes(value)
    elif choice == 3:
        print("Tchau!")
        break
        
    else:
        print("Escolha inválida. Por favor, tente novamente.")
