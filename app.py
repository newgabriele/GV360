import os
import streamlit as st

# Pagina configuratie voor GV360
st.set_page_config(
    page_title="GV360™ | Personal Command Center",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Styling voor de GV360 commandocentrale
st.markdown(
    """
    <style>
    .stApp {
        background-color: #121820;
        color: #e2e8f0;
    }
    h1, h2, h3 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #f8fafc;
    }
    .vault-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #334155;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
    }
    .status-online {
        color: #4ade80;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- SIDEBAR & NAVIGATIE ---
st.sidebar.title("GV360™ Control")
st.sidebar.markdown("---")
nav_choice = st.sidebar.radio(
    "Navigatie:",
    ["🏠 Command Dashboard", "🧬 Private Vault (Health & Energy)", "⚡ Bridge Status"],
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "**Status:** <span class='status-online'>SECURE & PRIVATE</span>",
    unsafe_allow_html=True,
)

# --- MAIN DASHBOARD ---
if nav_choice == "🏠 Command Dashboard":
  st.title("GV360™ — Personal Command Center")
  st.subheader("Welcome back, Gabriele.")

  st.markdown(
      """
        <div class="vault-card">
        <h4>🛡️ Holistische Besturing</h4>
        <p>Dit is je beveiligde commandocentrale. Hier komt de balans tussen je persoonlijke energie, welzijn en je professionele projecten (zoals Calibro360™) gecontroleerd samen.</p>
        </div>
        """,
      unsafe_allow_html=True,
  )

  col1, col2 = st.columns(2)

  with col1:
    st.markdown("### 📊 Vandaag overzicht")
    st.info(
        "Systeem operationeel. Private vault is gekoppeld en afgeschermd."
    )

  with col2:
    st.markdown("### 🔗 Snelle koppelingen")
    st.write("- Private Vault Vault-bestanden: **Actief**")
    st.write("- GitHub Repository: **Privé & Beveiligd**")

elif nav_choice == "🧬 Private Vault (Health & Energy)":
  st.title("🧬 Private Vault — Gezondheid & Energie")
  st.write(
      "Dit gedeelte leest rechtstreeks uit je beveiligde, lokale vault bestanden."
  )
  st.markdown("---")

  # Probeer het health profile in te lezen
  if os.path.exists("vault/health_profile.md"):
    with open("vault/health_profile.md", "r", encoding="utf-8") as f:
      profile_content = f.read()
    st.markdown("### Gezondheids- en Leefstijlelementen")
    st.markdown(
        f'<div class="vault-card">{profile_content}</div>',
        unsafe_allow_html=True,
    )
  else:
    st.warning("Vault profielbestand nog niet gevonden.")

  if os.path.exists("vault/energy_log.md"):
    with open("vault/energy_log.md", "r", encoding="utf-8") as f:
      energy_content = f.read()
    st.markdown("### Energie & Focus Log")
    st.markdown(
        f'<div class="vault-card">{energy_content}</div>',
        unsafe_allow_html=True,
    )

elif nav_choice == "⚡ Bridge Status":
  st.title("⚡ Business & Workflow Bridge")
  st.write(
      "Hier wordt de gecontroleerde verbinding gelegd tussen je persoonlijke"
      " gesteldheid en professionele output (zoals Calibro360™)."
  )
  st.markdown("---")
  st.info(
      "De brug is gereed om context (zoals energieniveau of focus) op een veilige"
      " manier door te vertalen naar je projecten."
  )
