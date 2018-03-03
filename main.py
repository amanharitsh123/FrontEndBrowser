#!/usr/bin/python3
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2
from gi.repository import Gtk

def main():
        Gtk.init()
        
        view = WebKit2.WebView()
        view.load_uri("http://localhost:8080/")
        window = Gtk.Window()
        window.add(view)
        window.set_decorated(False)
        window.maximize()
        window.show_all()
        Gtk.main()

main()
