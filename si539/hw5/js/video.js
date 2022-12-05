var vid

// page load 
window.addEventListener('load', function() {
    vid = document.querySelector('video')
    vid.removeAttribute('autoplay')
});

// play button
document.querySelector('#play').addEventListener('click', function() {
    console.log('Play Video');
    vid.play()
});

// pause button
document.querySelector('#pause').addEventListener('click', function() {
    console.log('Pause Video');
    vid.pause()
});

// slow down
document.querySelector('#slower').addEventListener('click', function() {
    // need to set a range of the speed
    // let playspeed = vid.playspeed;
    if (vid.playbackRate === 0.5) {
        window.alert("Video is at slowest speed!");
    }
    else if (vid.playbackRate === 1) {
        vid.playbackRate = 0.5;
    }
    else if (vid.playbackRate === 2) {
        vid.playbackRate = 1;
    }
});

// speed up
document.querySelector('#faster').addEventListener('click', function() {
    if (vid.playbackRate === 2) {
        window.alert("Video is at fastest speed!");
    }
    else if (vid.playbackRate === 1) {
        vid.playbackRate = 2;
    }
    else if (vid.playbackRate === 0.5) {
        vid.playbackRate = 1;
    }
});

// skip ahead 
document.querySelector('#skip').addEventListener('click', function() {
    let skiptime = vid.currentTime + 15;
    if (skiptime > vid.duration) {
        vid.currentTime = 0;
    }
    else {
        vid.currentTime = skiptime;
    }
});

// mute
document.querySelector('#mute').addEventListener('click', function() {
    if (vid.muted) {
        document.querySelector('#mute').innerHTML = 'Mute';
        vid.muted = false;
        document.getElementById('slider').value = 100;
        document.querySelector('#volume').innerHTML = 100;
    }
    else {
        document.querySelector('#mute').innerHTML = 'Unmute';
        vid.muted = true;
        document.getElementById('slider').value = 0;
        document.querySelector('#volume').innerHTML = 0;
    }
});

// volume slider 
document.querySelector('#slider').addEventListener('click', function() {
    let vol = document.getElementById('slider').value;
    document.querySelector('#volume').innerHTML = vol;
})