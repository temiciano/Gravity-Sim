Simple simulation to understand what needs a rocket to leave influence of gravity solar system. And goal a point with no gravity, a point with only innercy.


<p align="center">
  <img src="/example_1.png" width="500" alt="Diagrama del sistema"/>
</p>


This documentation will be updated as project progresses


The first thing we want to do is identify all bodies we need in this simulation.
In this case there will only be 3, the sun, the planet and the rocket will be leave the planet.
Orientes object programing will be key for this aspect. This because the tree elements share the same properties (mass, position, velocity).

https://github.com/temiciano/Gravity-Sim/blob/0544bacfec56e68a97f578f74c3dbef95f9eb0bd/main.py#L7-L12

We have assigned ot objects, now we need create the physics.
We will use Newton's laws to representate the system.
In this case the constant universal gravity we will asign the arbitrary value of 1.


before apply the ecuation must make little adjust in the calculations.
Calcule the difference between two bodies.

https://github.com/temiciano/Gravity-Sim/blob/0544bacfec56e68a97f578f74c3dbef95f9eb0bd/main.py#L30-L31

This value will be delibered to us as a vector, example "(2,4)", this is useless to apply in the simulation. We must convert to numbre and thats use how distance. 


Variable "force" we got magnitude, and with him we got acceleration.
Then to obtain direction, we use vector "distance" calculated before and dividing by its owns magnitude.

https://github.com/temiciano/Gravity-Sim/blob/0544bacfec56e68a97f578f74c3dbef95f9eb0bd/main.py#L37-L41

Now, we make all logic created previously shows in our screen.
Def refresh(frame)

Let's apply values obtaindes from functoin "calc_acceleration" to elements planet and sun. What take place of "body" and "attractor" respectively.
And we add to real velocity, and this is going to apply 1 time per tick.
Finally, we apply this resulting velocity to the planet's position, once per tick, which results in the body moving to the position calculated by the integrator.


Finally, draw the function


Now we have basic pseudo solar system, just a planet orbiting a sun.

To do:
Add perihelion to accurate simulate orbital bodies
Add rocket, launches after x seconds.