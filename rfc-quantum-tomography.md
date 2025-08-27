---
###
# Internet-Draft Markdown Template
#
# Rename this file from draft-todo-yourname-protocol.md to get started.
# Draft name format is "draft-<yourname>-<workgroup>-<name>.md".
#
# For initial setup, you only need to edit the first block of fields.
# Only "title" needs to be changed; delete "abbrev" if your title is short.
# Any other content can be edited, but be careful not to introduce errors.
# Some fields will be set automatically during setup if they are unchanged.
#
# Don't include "-00" or "-latest" in the filename.
# Labels in the form draft-<yourname>-<workgroup>-<name>-latest are used by
# the tools to refer to the current version; see "docname" for example.
#
# This template uses kramdown-rfc: https://github.com/cabo/kramdown-rfc
# You can replace the entire file if you prefer a different format.
# Change the file extension to match the format (.xml for XML, etc...)
#
###
title: "Quantum Tomography in JavaScript Object Notation (JSON)"
abbrev: "QT-JSON"
category: info

docname: rfc-quantum-tomography
submissiontype: IRTF
number:
date:
consensus: true
v: 3
area: Quantum Information
workgroup: QIRG
keyword:
 - quantum state
 - teleportation
 - superposition
 - entanglement
 - quantum key distribution
 - distributed quantum computing
venue:
  group: Quantum Internet Reserach Group
  type: Working Group
  mail: qirg@irtf.com
  arch: https://example.com/WG
  github: USER/REPO
  latest: https://example.com/LATEST

author:
 -
    fullname: Roger Selly
    organization: Panvia Future Technologies Inc.
    email: roger@panviaquantum.com

normative:

informative:

...

--- abstract

Quantum state information exchange in a network is a foundational technology for distributed quantum computation. Multi-qubit entangled state quantum information is represented as structured data in the application/json media type. The collective state of the connected qubits is represented in a multiverse superposition described mathematically as a quantum possibility space, QPS, of different qubit state combinations. The QPS is designed as an intermediate between quantum gate circuits that preserves qubit superposition and entanglement states and allows their subsequent quantum algorithmic processing without any state collapsing observations. The essential components are specified by their type, function and structured form to provide a general template for a lightweight, text-based, operating system-independent quantum computing and quantum communication data interchange format.

--- middle

# Introduction

Quantum information is functionally different from binary information because it incorporates the quantum effects of superposition and entanglement. These two phenomena are created by quantum gates in a circuit of connected quantum bits, or qubits. Qubits can be in any combination of the ground state |0> and the excited state |1> as a superposition. The result of a Conditional NOT, CNOT, quantum gate between a control qubit and a target qubit is entangled states of the pair in which particular |0>/|1> qubit pair-wise combinations are formed and become alternatives. Recently, the Fock space of an evolving Hamiltonian was formulated as a sum over a finite set of indices and operators with conjugate product coefficients that are complex and non-zero [DG].

1.1. Distributed Quantum Computing Goal

The presentation of a Quantum Possibility Space in this RFC is intended to empower developers by providing a new and practical way to share quantum information via the current internet. The ability to transfer quantum tomography between systems enables an important new distributed quantum computing paradigm in which networking can deliver unprecedented scalability for quantum computing. The goal of this RFC is therefore to promote distributed quantum computing in an open community as would befit the ideals of Jon Postel.

# Conventions and Definitions

{::boilerplate bcp14-tagged}

The key words "MUST" and "SHOULD" in this document are interpreted as described in [RFC2119]. 


# Security Considerations

TODO Security


# IANA Considerations

This document has no IANA actions.


--- back

# Acknowledgments
{:numbered="false"}

TODO acknowledge.
