from fluvel import FluvelApp

# App
app = FluvelApp()

app.register(initial="sign-in-page")

if __name__ == "__main__":
    app.run()