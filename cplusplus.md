C++
===================

#### What's the proper use of printf to display pointers padded with 0s

[stackoverflow](http://stackoverflow.com/questions/1255099/whats-the-proper-use-of-printf-to-display-pointers-padded-with-0s)

```c++
#include <inttypes.h>
#include <stdint.h>
printf("%016" PRIxPTR "\n", (uintptr_t)ptr);
```

[Linux performance tools](http://www.tecmint.com/command-line-tools-to-monitor-linux-performance/)

#### Htop








