import "CategoryDelegate.qml";
import controls.HighlightListView;

import "js/constants.js" as constants;

HighlightListView {
    id: categoryList;

    focus: true;
    clip: true;
    hlWidth: 4;
    hlHeight: 4;
    highlightColor: "#0f66e9";

    model: ListModel {}

    delegate: CategoryDelegate {}

    onCompleted: {
        constants.categories.forEach(function (category) {
            model.append( { title: category.title, url: category.url });
        });
    }
}
