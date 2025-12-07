basic.forever(function () 
    for (let i = 0; i < 5; i++) 
        led.plot(i, 2)
        basic.pause(100)
        led.unplot(i, 2)

)
