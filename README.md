# kivy-rein

Mobile app using the kivy framework for the Rein decentralized freelance market

## Build instructions

To compile this application for use on Android, install the latest version of the packaging tool Buildozer. Follow the steps outlined [here](https://kivy.org/docs/guide/packaging-android.html). Then, install all necessary python dependencies by running `pip install -r requirements.txt` (on Linux use `source pip_install.sh`, which will skip Windows-only dependencies). Lastly, run `buildozer android_new debug`.

Please note that to run Kivy on your PC, perhaps also to compile the app successfully, additional dependencies may have to be downloaded. Please refer to [Kivy's official documentation](https://kivy.org/docs/installation/installation.html) for further information.
