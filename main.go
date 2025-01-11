package main

import (
    "fmt"
    "log"
    "net/http"
)

func main() {
    templatesFileServer := http.FileServer(http.Dir("./templates"))
    http.Handle("/", templatesFileServer)

    staticFileServer := http.FileServer(http.Dir("./static"))
    http.Handle("/static/", http.StripPrefix("/static/", staticFileServer))

    fmt.Printf("Starting server at port 8080\n")

    if err := http.ListenAndServe(":8080", nil); err != nil {
        log.Fatal(err)
    }
}
