package main

import (
    "fmt"
    "os"
    "os/exec"
    "syscall"
)

func main() {
    switch os.Args[1] {
    case "run":
         run()
    case "child":
        child()
    default:
        panic("help")
    }
}

func run() {
    fmt.Printf("Running %v as pid %d\n", os.Args[2:], os.Getpid())

    cmd := exec.Command("/proc/self/exe", append([]string{"child"}, os.Args[2:]...)...)
    cmd.Stdin = os.Stdin
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr
    cmd.SysProcAttr = &syscall.SysProcAttr {
        Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWPID,
    }

    must(cmd.Run())
}

func child() {
    fmt.Printf("Running %v as pid %d\n", os.Args[2:], os.Getpid())
  
    cmd := exec.Command(os.Args[2], os.Args[3:]...)
    cmd.Stdin = os.Stdin
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr

    must(syscall.Sethostname([]byte("container")))

    syscall.Chroot("./ROOT_DIR")
    syscall.Chdir("/")

    must(cmd.Run())
}
  
func must(err error) {
  if err != nil {
    panic(err)
  }
}
