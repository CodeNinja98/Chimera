# main.py - Point d'entrée du Projet Chimera
import sys
from utils import Agent, Simulation

def run_simulation(num_agents, duration):
    print(f"Lancement de la simulation Chimera avec {num_agents} agents pour {duration} secondes...")
    sim = Simulation(num_agents)
    sim.start()
    # Logique de simulation...
    sim.stop()
    print("Simulation terminée.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py <num_agents> <duration_seconds>")
        sys.exit(1)

    num_agents = int(sys.argv[1])
    duration = int(sys.argv[2])
    run_simulation(num_agents, duration)
