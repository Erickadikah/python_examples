public class Insertion{
    public void sort(int[] array){
        for (var i = 1; i < array.lenth; i++ ) {
            va current = array [i];
            var j = i -1;
            while (j >= 0 && array[j] > current){
                array[j + 1] = array [j];
                j--;
            }
        }array [j + 1] = current;
    }
}