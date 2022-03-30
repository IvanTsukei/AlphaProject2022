from frontend.main import App
import backend.storage as storage


def main():
    data = storage.read_data()
    data['profiles'].append({})
    storage.write_data(data)

    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
