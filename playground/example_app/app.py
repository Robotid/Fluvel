from fluvel import FluvelApp

# App
app = FluvelApp()

app.register(initial="github-badges-example")

if __name__ == "__main__":
    app.run()