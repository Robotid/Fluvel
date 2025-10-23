from fluvel.composer.Factory import Factory


@Factory.compose(target="FLabel")
def InfoLabel(text: str):
    return {"text": text, "style": "info"}


@Factory.compose(target="FLabel")
def WarningLabel(text: str):
    return {"text": text, "style": "warning"}


@Factory.compose(target="FLabel")
def DangerLabel(text: str):
    return {"text": text, "style": "danger"}


@Factory.compose(target="FLabel")
def SuccessLabel(text: str):
    return {"text": text, "style": "success"}
