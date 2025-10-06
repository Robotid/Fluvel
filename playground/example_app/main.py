from fluvel import FluvelApp

# App
app = FluvelApp()

app.register(initial="login")

if __name__ == "__main__":
    app.run()