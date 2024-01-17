package main

import (
    "fmt"
    "os"
    "os/exec"
    "syscall"
    "path/filepath"
    "io/ioutil"
    "strconv"
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
        Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWPID | syscall.CLONE_NEWNS,
        // Unshareflags: syscall.CLONE_NEWNS,
    }

    must(cmd.Run())
}

func child() {
    fmt.Printf("Running %v as pid %d\n", os.Args[2:], os.Getpid())
  
    cg()

    cmd := exec.Command(os.Args[2], os.Args[3:]...)
    cmd.Stdin = os.Stdin
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr

    must(syscall.Sethostname([]byte("container")))

    syscall.Chroot("./ROOT_DIR")
    syscall.Chdir("/")

    syscall.Mount("proc", "proc", "proc", 0, "")

    must(cmd.Run())

    syscall.Unmount("proc", 0)
}
  
func must(err error) {
  if err != nil {
    panic(err)
  }
}

func cg() {
    cgroups := "/sys/fs/cgroup/"
    pids := filepath.Join(cgroups, "pids")
    os.Mkdir(filepath.Join(pids, "hyun"), 0755)
    must(ioutil.WriteFile(filepath.Join(pids, "hyun/pids.max"), []byte("10"), 0700))
    // Remove the new cgroup in place after the container exits
    must(ioutil.WriteFile(filepath.Join(pids, "hyun/notify_on_release"), []byte("1"), 0700))
    must(ioutil.WriteFile(filepath.Join(pids, "hyun/cgroup.procs"), []byte(strconv.Itoa(os.Getpid())), 0700))
}
