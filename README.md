# Inkscape Travel Extension

Copy an object along a precise parametric trajectory.

Two objects must be selected to use this extension: a rectangle and a template. The rectangle must be below the template, and the template must be a path or group of paths. If any path within the template has "arc" elements (e.g. ellipse/arc objects that have been converted to paths) you will encounter errors using the rotation function.

Specify the timepoints at which your template will be copied using "start time", "end time", and either "number of steps", "fps", or "time interval". For example, if "start time" is 1, "end time" is 2, and "number of steps" is 6, then 6 copies of the template will be made, corresponding to times 1, 1.2, 1.4, 1.6, 1.8, and 2.0. If "number of steps" is zero, then "fps" can be used to specify frames per second, and if "fps" is also zero, "time interval" can be used to specify the interval between time points from "start time" to "end time".

Example 1:

![cosine_1](cosine_1.png "Cosine 1") 

![cosine_2](cosine_2.png "Cosine 2") 
