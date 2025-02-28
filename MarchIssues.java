public class MarchIssues {
    public static void main(String[] args){

        String[] interests = {"Heavenly Tyrant", "Basiskennis Wiskunde", "She-Ra", "Java"};

        System.out.println(interests[0]);

        String[] topics = new String[4];

        topics[0] = "Heavenly Tyrant";
        topics[1] = "Algebra";
        topics[2] = "She-Ra";
        topics[3] = "Java W3";

        for(int i=0; i<topics.length; i++){
            System.out.println(topics[i]);
        }

        String[] xmen = new String[10];

        xmen[0] = "X-Men";
        xmen[1] = "Uncanny X-Men";
        xmen[2] = "Ultimate X-Men";
        xmen[3] = "Storm";
        xmen[4] = "Psylocke";
        xmen[5] = "Magik";
        xmen[6] = "Avengers";
        xmen[7] = "Ultimate Wolverine";
        xmen[8] = "";
        xmen[9] = "";

        for(int i=0; i<xmen.length; i++){
            System.out.println(xmen[i]);
        }

        String[] marvelBooks = new String[2];

        marvelBooks[0] = "Ultimates";
        marvelBooks[1] = "Ultimate Spider-Man";
        marvelBooks[2] = "";
        marvelBooks[3] = "";

        for(int i=0; i<marvelBooks.length; i++){
            System.out.println(marvelBooks[i]);
        }

        String[] dcBooks = new String[4];

        dcBooks[0] = "Absolute Wonder Woman";
        dcBooks[1] = "Absolute Martian Manhunter";
        dcBooks[2] = "Absolute Green Lantern";
        dcBooks[3] = "Catwoman";

        for(int i=0; i<dcBooks.length; i++){
            System.out.println(dcBooks[i]);
        }

        String[] achillesHeel = new String[5];

        achillesHeel[0] = "Math";
        achillesHeel[1] = "Java";
        achillesHeel[2] = "JavaScript";
        achillesHeel[3] = "PHP";
        achillesHeel[4] = "Espanol";

        for(int i=0; i<achillesHeel.length; i++){
            System.out.println(achillesHeel[i]);
        }


}
}