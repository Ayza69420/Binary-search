function binarySearch(array, tar) {
    var l = 0;
    var r = array.length-1;

    while (l <= r) {
	    var m = Math.round((l+r)/2)

	    if (tar == array[m]) { return m }

	    else if (tar < array[m]) { r = m-1 }

	    else { l = m+1 }
    }

  return -1
}
