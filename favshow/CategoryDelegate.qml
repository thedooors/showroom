import "js/constants.js" as constants;

BodyText {
    id: categoryText;

    text: model.title;

    color: categoryText.activeFocus ? constants.colors["active"] : "#000000";
}

