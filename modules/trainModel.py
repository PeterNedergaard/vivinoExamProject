from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


def get_model(X, y):
    model = DecisionTreeClassifier()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10)

    model.fit(X_train, y_train)

    return model, X_train, X_test, y_train, y_test
