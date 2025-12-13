package main

import (
	"bytes"
	"fmt"
	"os"

	"github.com/brianvoe/gofakeit"
)

func main() {
	var buf bytes.Buffer
	for range 1000 {
		fmt.Fprintln(&buf, gofakeit.FirstName())
	}

	if err := os.WriteFile("names.txt", buf.Bytes(), 0666); err != nil {
		panic(err)
	}
}
