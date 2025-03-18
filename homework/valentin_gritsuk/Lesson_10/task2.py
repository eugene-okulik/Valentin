def repeat_me_how_many_times(count):

    def repeat_me(func):

        def wrapper(text):
            results = []  # Для сохранения ретурнов, если таковые есть у декорируемой функции для универсальности
            for _ in range(count):
                results.append(func(text))
            return results
        return wrapper

    return repeat_me


@repeat_me_how_many_times(count=5)
def example(text):
    print(text)


example('print me')
