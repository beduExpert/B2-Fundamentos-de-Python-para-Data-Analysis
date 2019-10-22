 `Fundamentos de Python para Data Analysis`> `[Sesión 08]`  
  
## Postwork

### OBJETIVO 
 - Identificar los conceptos de clusterización y redes neuronales. Conocer sobre otros métodos de clasificación – o bien, las redes neuronales y/o las K-medias.  

#### DESARROLLO
**Acerca de la clusterización y las redes neuronales:**  

En esta sesión hemos visto las herramientas más comunes para poder hacer agrupación de datos, clasificación binaria, y clasificación multi-clase. No hemos tenido que tratar la matemática detrás de cómo funcionan, sin embargo es importante que tengas una noción más a profundidad si planeas crear algoritmos de clasificación más poderosos. Sin embargo, para tu proyecto estos algoritmos puede que sean suficientes. Si tienes más curiosidad sobre otros métodos de clasificación – o bien, las redes neuronales y/o las K-medias no están resolviendo tu problema- puedo sugerirte los siguientes tips:  

**Tips:**  

Hay una alternativa a redes neuronales llamada “Máquinas de soporte vectorial” (SVM) que incluye SciKitLearn, y puede serte de utilidad. Ojo, Deep Learning y SVM no se llevan muy bien que digamos, y si planeas avanzar hacia Deep Learning, SVM puede no ser la mejor idea… https://scikit-learn.org/stable/modules/svm.html   

Para la agrupación de datos puedes utilizar también el algoritmo de propagación por afinidad (affinity propagation) que se encuentra descrito aquí: https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html   

Un mapa auto-organizativo (SOM) es un híbrido entre redes neuronales y agrupación. Te permite reducir un hiperplano n-dimensional en un mapa de 2 dimensiones, lo cual puede serte útil para categorizar o crear sistemas de recomendación, puedes revisar de ello aquí:
https://towardsdatascience.com/self-organizing-maps-ff5853a118d4 


