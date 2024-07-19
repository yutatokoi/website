---
publishDate: "2024-07-05"
---

# Formal Methods

At this point, my understanding of formal methods in software developemnt is very fuzzy. So much so, I don't understand when to appropriately use "formal methods" and "formal verification", or what the exact differences between them are.

This is my attempt to organise this fuzzy understanding into something more concrete, as well as a record to reflect on in the futuere. This is a topic that has captivated my attention as of late, and is something I will continue diving deeper into. In the future, I hope to look back on this and be able to point out inaccuracies and holes in my understanding.

## What is formal methods

Formal methods is the application of mathematically rigorous methods to prove properties of software/hardware.

Formal methods in vericiation: formal methods can be applied to prove the properties of already existing software.

Formal methods in specification: formal methods can be used to create specifications for software that is to be built, such that it will behave according to specifications.

## Why formal methods

Formal methods is firstly most important in verifying software that requires complete accuracy and reliability. As software becomes more widely and deeply integrated into everything, some software can turn out to be critical. At times, even a matter of life and death. The software for a pacemaker abruptly stopping could end the life of the person using it. The cooling system for a nuclear power plant not cooling the reactor sufficiently could lead to catastrophic futures.

When applied during specification stages, formal methods has the ability to reduce significant work and costs in later stages of software development. It is common to find bugs or unexpected behavior when developing software, or even worse, in deployment. An error in deployment can lead to direct harm to users, company profits, and reputation. An error found during later stages of software development can setback long periods of work, leading to more time and money spent on development, as well as adding to mental/emotional fatigue for everyone involved.

## Why not formal methods

When the upsides are so alluring, why is formal methods not something more mainstream?

For one, it is very time consuming. Like how writing a formal mathematical proof is time consuming, so is the formal verification of software. It is currently impractical for human programmers to prove the properties vast quantities of software (there are significant efforts into fully/partially automating formal verification).

For this reason, it is simply not appropriate for many scenarios. Especially if the specification/design/features of a piece of software is constantly changing or growing, the effort to formally prove its properties can not keep up.

It may not even be necessary in some cases. Proving that my toy implementation of a tic-tac-toe playing program written for myself has correctly implemented the Minimax algorithm is overkill.

Formalised specifications may not be 100% replicated in the production version. The formalisation process is done in an abstract form, often in a completely separate programming language to the deployment implementation. What is to guarantee that the real world implementation follows the exact specification that was proven in the formalisation?

## Where is formal methods

Medical devices, nuclear power plants, aviation

Amazon Web Services (Automated Reasoning Group), Microsoft (RiSE), Facebook

Hardware verification (this is outside of formal methods in software, but it is very prevalent in industry)

## How is formal methods

Programming languages: Coq, Agda, Lean, Dafny, Cedar, TLA+

