# Day 1 at Knull




## The Project

To learn and adopt the method in which professional engineers work before they begin a large task




### What I'm learning 


- A **Repository** is a project folder that Git tracks

- A **commit** is a saved, annotated snapshot of my changes

- A **branch** is a smaller wing of work that can later be merged back into the 
main

- A **Markdown** is a simple way to use formatting in plain files

- **Ship small** means to make small, working changes at a time, committing them as you go



# Day 2 at Knull



## The Project



The problem can be initially described in plain English, acting as a guide for later code to follow:


Shoppers arrive at the till randomly, at an average rate of λ (lambda people) per minute. The till serves one shopper at a time, at an average rate of μ (mu people) per minute. If a shopper arrives while the till is still busy with someone else, they queue and wait. The value we care about is W — the average time each shopper spends in the system (waiting + being served). If shoppers arrive faster than the till can serve them (λ ≥ μ), then the queue never empties and W continuously grows. 



### 'Cliff' Write-up



As λ approaches μ (arrivals rate approaches the till's serving capacity), the average wait time rises rapidly. Going from λ=1.0 to λ=1.4 (a 40% increase) only raises wait from 1.0 to 1.67 minutes. But going from λ=1.8 to λ=1.9 (just a 5.5% increase) doubles the wait, from 5.0 to 10.0 minutes. This is the "cliff", because if we take: W = 1/(μ−λ), the denominator shrinks toward zero as λ approaches μ, so W grows towards infinity. 


For a business, this means running a till near full capacity can be risky as a small increase in footfall can cause a disproportionate spike in queue times.





### About me



Hi, I'm Alex - currently learning software engineering fundamentals through this logbook