from fluvel import FluvelApp

# App
app = FluvelApp()

app.register(
    initial="login", 
    views=[
        "views.login", 
        "views.home", 
        "views.hello_world",
        "views.hot_reload_example"
    ]
)


if __name__ == "__main__":
    app.run()
