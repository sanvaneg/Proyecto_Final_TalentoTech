import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def generate_bar_graph():
  years = list(range(1965, 2023))
  wind = np.random.randint(5, 50, size=5).cumsum()
  solar = np.random.randint(1, 40, size=5).cumsum()
  hydroelectric = np.random.randint(10, 100, size=5).cumsum()
  biomass = np.random.randint(1, 20, size=5).cumsum()

  bar_width = 0.2
  x = np.arange(5)

  plt.bar(x - bar_width * 1.5, wind, width=bar_width, label="eolica", color="blue")
  plt.bar(x - bar_width / 2, solar, width=bar_width, label="Solar", color="yellow")
  plt.bar(x + bar_width / 2, hydroelectric, width=bar_width, label="Hydroelectrict", color="green")
  plt.bar(x + bar_width * 1.5, biomass, width=bar_width, label="Biomass", color="brown")

  plt.xlabel("Year")
  plt.ylabel("Energy Production (TWh)")
  plt.title("Renewable Energy Production by Source (1965 - 2022)")
  plt.xticks(x, list(range(1, 6)), rotation=45)
  plt.legend()

  plt.tight_layout()
  plt.savefig("/workspaces/sanvaneg.github.io/Avances_Proyecto_Final/templates/assets/imgs/bar_graph.png")
  plt.close()
  plt.show()

from flask import Flask, render_template
from graph_generator import generate_bar_graph

app = Flask(__name__)

@app.route("/")
def home():
    generate_bar_graph()
    return render_template("HidroEcoEquidad.html") 