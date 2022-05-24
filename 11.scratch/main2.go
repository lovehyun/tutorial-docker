package main

import (
  "fmt"
  "os"
  "os/exec"
)

// go run main.go run echo hello world
// go run main.go run ls -l
func main() {
  switch os.Args[1] {
  case "run":
    run()
  default:
    panic("help")
  }
}

func run() {
  fmt.Printf("Running %v as pid %d\n", os.Args[2:], os.Getpid())

  cmd := exec.Command(os.Args[2], os.Args[3:]...)
  cmd.Stdin = os.Stdin
  cmd.Stdout = os.Stdout
  cmd.Stderr = os.Stderr

  must(cmd.Run())
}

func must(err error) {
  if err != nil {
    panic(err)
  }
}
