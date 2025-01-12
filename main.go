package main

import (
    "fmt"
    "log"
    "net/http"
    "path/filepath"
)

func serveTemplate(w http.ResponseWriter, r *http.Request) {
    requestedPath := r.URL.Path
    if requestedPath == "/" {
        requestedPath = "index.html"
    } else {
        requestedPath += ".html"
    }

    filePath := filepath.Join("./templates", requestedPath)

    http.ServeFile(w, r, filePath)
}

func main() {

    http.HandleFunc("/", serveTemplate)

    staticFileServer := http.FileServer(http.Dir("./static"))
    http.Handle("/static/", http.StripPrefix("/static/", staticFileServer))

    fmt.Println("Starting server at port 8080")

    if err := http.ListenAndServe(":8080", nil); err != nil {
        log.Fatal(err)
    }
}
