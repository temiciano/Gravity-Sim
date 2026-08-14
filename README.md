Simulación simple para comprender que necesita un cohete para abandonar la influencia de la gravedad solar y planetaria, hasta llegar al punto de movimiento por inercia.

Simple simulation to understand what needs a rocket to leave affluence of gravity solar system. And goal a point with no gravity, a point with only innercy.


Esta documentación se irá actualizando a medida que avance el proyecto

This documentation will be updated as project progresses


Lo primero que querriamos hacer es identificar todos los cuerpos que formaran parte de la simulacion.
En este caso solo son 3, El sol, el planeta, y el cohete que saldra del planeta.
Para eso utilizaremos La programacion orientada a objetos. Ya que nuestros 3 elementos necesitaran las mismas propiedades (masa, posicion, velocidad)

This first thing what want to do is identify all bodies we need in this simulation.
In this case there will only be 3, the sun, the planet and the rocket will be leave the planet.
Orientes object programing will be key for this aspect. This because the tree elements share the same properties (mass, position, velocity).


Tenemos asignados nuestros objetos, ahora hay que crear la fisica.
Usaremos las leyes de newton, para representar el sistema.
En este caso a la constante de gravitacion universal le daremos el valor arbitrario de 1. 

Have assigned ot objects, now we need create the physics.
With the newton's law to representate the system.
In this case the constant universal gravity we will asign the arbitrary value of 1.


before apply the ecuation must make little adjust in the calculus.
Calcule the difference between two bodies.
""distance = body.pos - attractor.pos""

Antes de aplicar la ecuacion directamente debemos hacer unos ajustes en los calculos.
Calculamos la diferencia de posicion entre dos cuerpos.


Este valor nos sera entregada como vector, por ejemplo "(2,4)", lo cual no nos sirve para la formula. Debemos convertirlo a numero y asi usarlo como distancia.

This value will be delibered to us as a vector, example "(2,4)", this is useless to apply in the simulation. Will be convert to numbre and thats use how distance. 


Ahora tenemos un valor "r" que si mide distancia y elevamos a 2.
Now we have a value "r", this is usefull to measure distance and square.



Con force obtenemos la magnitud, pero la magnitud por si sola no nos sirve de mucho, nos falta la aceleracion y direccion.
force = numerator / denominator


Ahora debemos hacer que toda la logica creada anteriormente se muestre en pantalla. 

Def refresh(frame)

Aplicaremos los valores obtenidos de la funcion "calc_acceleration" a los elementos planet y sun. Que toman el lugar de "body" y "attractor" respectivamente.
a = calc_acceleration(planet, sun)
Y se lo sumamos a su velocidad real, el cual se aplicara 1 vez por tick.
planet.vel = planet.vel + a * tick
Y esta velocidad resultante se la aplicamos a la posicion del planeta, 1 vez por tick, lo que nos dara como resultado que body se mueva a la posicion que calculo el integrador.
planet.pos = planet.pos + planet.vel * tick

Finalmente dibujamos la funcion.
