import random

class MiningTools:
    money = 100
    ores = 0
    workers_created = 0

    def __init__(self, mining_power, cost):
        self.mining_power = mining_power
        self.cost = cost
        MiningTools.workers_created += 1

    def mine_ore(self):
        MiningTools_ores += self.mining_power

    def show_workers_created(self):
        print("Total mining workers created:", MiningTool.workers_created)

class MiningExpert(MiningTools):
    def __init__(self,mining_power = 10, cost = 20):
        super().__init__(mining_power, cost)

class MiningDrill(MiningTools):
    def __init__(self, mining_power = 20, cost = 50, drilling_power = 1.1):
        super().__init__(mining_power, cost)
        self.drilling_power = drilling_power

    def mine_ore(self):
        if random.random() < 0.3:
            effective_mining_power = self.mining_power * self.driling_power
        else:
            effective_mining_power = self.mining_power

        return effective_mining_power

class MiningBulldozer(MiningTools):
    def __init__(self, mining_power = 30, cost = 100, drilling_power = 1.5):
        super().__init__(mining_power, cost)
        self.drilling_power = drilling_power

    def mine_ore(self):
        if random.random() < 0.5:
            effective_mining_power = self.mining_power * self.drilling_power
        else:
            effective_mining_power = self.mining_power

        return effective_mining_power

def main():
    mining_experts = []
    mining_drills = []
    mining_bulldozers = []
    while True:
        print("\n=== Mining Simulator Menu ===")
        print("Press Enter to continue mining")
        print("Enter 1 to view total mining power, number of ores, and money")
        print("Enter 2 to view the total number of different mining equipment")
        print("Enter 3 to change ores into money")
        print("Enter 4 to purchase mining equipment")
        print("Enter Q to quit the game")

        choice = input("Choose an option: ").lower()

        if choice == "":
            total_ores_mined = 0
            for expert in mining_experts:
                expert.mine_ore()

            for drill in mining_drills:
                total_ores_mined += drill.mine_ore()

            for bulldozer in mining_bulldozers:
                total_ores_mined += bulldozer.mine_ore()

            MiningTools.ores += total_ores_mined
            print("Mined ores. Total ores:", MiningTools.ores)

        elif choice == "1":
            total_mining_power = 0
            for expert in mining_experts:
                total_mining_power += expert.mining_power

            for drill in mining_drills:
                total_mining_power += dril.mining_power * drill.drilling_power

            for bulldozer in mining_bulldozers:
                total_mining_power += bulldozer.mining_power * bulldozer.drilling_power

        elif choice == "2":
            if mining_experts:
                mining_expert[0].show_workers_created()

            elif mining_drills:
                mining_drill[0].show_workers_created()

            elif mining_bulldozers:
                mining_bulldozer[0].show_workers_created()

            else:
                print("No workers created yet.")

            print("Mining Experts:", len(mining_experts))
            print("Mining Drills:", len(mining_drills))
            print("Mining Bulldozers:", len(mining_bulldozers))

        elif choice == "3":
            MiningTools.money += MiningTools.ores
            print("Converted ", MiningTools.ores," ores into money. Total money:", MiningTools.money)
            MiningTools.ores = 0

        elif choice == "4":
            print("\n=== Purchase Mining Equipment ===")
            print("1. Mining Expert ($20)")
            print("2. Mining Drill ($50)")
            print("3. Mining Bulldozer ($100)")
            equipment_choice = input("Choose equipment to purchase: ")

            if equipment_choice == "1":
                if MiningTools.money >= 20:
                    mining_experts.append(MiningExpert())
                    MiningTools.money -= 20
                    print("You Purchased A Mining Expert")
                else:
                    print("Not Enough Money To Purchase A Mining Expert")

            elif equipment_choice == "2":
                if MiningTools.money >= 50:
                    mining_drills.append(MiningDrill())
                    MiningTools.money -= 50
                    print("You Purchased A Mining Drill")
                else:
                    print("Not Enough Money To Purchase A Mining Drill")

            elif equipment_choice == "3":
                if MiningTools.money >= 100:
                    mining_bulldozers.append(MiningBulldozer())
                    MiningTools.money -= 100
                    print("You Purcased A Mining Bulldozer")
                else:
                    print("Not Enough Money To Purchase A Mining Bulldozer")
            else:
                print("Invalid Option. Please Try Again")

        elif choice == "q":
            print("Quitting the game. Goodbye!")
            break
        else:
            print("Invalid option. PLease try again")

main()
