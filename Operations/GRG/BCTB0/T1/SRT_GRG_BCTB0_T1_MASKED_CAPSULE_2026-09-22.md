---
type: masked-capsule-candidate
status: candidate
canonical: false
---

R2 T1 CAPSULE FACTS

FACT 1 =
In a clustered container platform, application workloads run as network-addressable units and commonly carry metadata labels.

FACT 2 =
A declarative configuration object can select workload units by metadata and contain separate rule sections for incoming and outgoing traffic.

FACT 3 =
Rule entries can identify peers by workload metadata, namespace metadata, or IP address ranges, and can also refer to transport protocols and ports.

FACT 4 =
More than one such configuration object can select the same workload unit.

self-check:
target/product/feature name exposed = NO
expected discriminator exposed = NO
expected false positive exposed = NO
expected failure condition exposed = NO
later result consulted = NO
