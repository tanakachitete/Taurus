// Obtained from Tanaka Chitete
// (accessed 22/10/2020)

/*
 * NAME: UnitTestDSAHashSet
 * CREATOR: Tanaka Chitete
 * STUDENT_ID: 20169321
 * UNIT: COMP1002
 * PURPOSE: Perform various operations in regards to hash set
 * CREATION: 28/09/2020
 * LAST MODIFICATION: 22/10/2020
 */

public class SetTestHarness {
    public static final int QUIT = 0;
    public static final int OPTION_1 = 1;
    public static final int OPTION_2 = 2;
    public static final int OPTION_3 = 3;
    public static final int OPTION_4 = 4;

    public static void main(String[] args) {
        int sel;
        Set<String> set = new Set<String>();
        do {
            System.out.println("Main Menu\n\n" + 
                "1. Add\n" +
                "2. Remove\n" +
                "3. Contains\n" +
                "4. Print\n" +
                "0. Quit\n");
            String prompt = "Selection: ";
            sel = UserInterface.userInput(QUIT, OPTION_4, prompt);

            switch (sel) {
                // User input specifies "Add Entry"
                case 1:
                    add(set);
                    break;
                // User input specifies "Remove Entry"
                case 2:
                    remove(set);
                    break;
                // User input specifies "Contains"
                case 3:
                    contains(set);
                    break;
                // User input specifies "Display"
                case 4:
                    print(set);
                    break;
            }
        }
        while (sel != QUIT);
    }

    /*
     * NAME: addEntry
     * IMPORT(S): set (DSAHashSet)
     * EXPORT(S): NONE
     * PURPOSE: Add entries into hash tables
     * CREATION: 28/09/2020
     * LAST MODIFICATION: 22/10/2020
     */

    private static void add(Set<String> set) {
        System.out.println("\nAdd\n");

        try {
            String prompt = "Element: ";
            String value = UserInterface.userInput(prompt);
            set.add(value);
            System.out.println();
        }
        catch (IllegalArgumentException e) {
            System.out.println("\n" + e.getMessage() + "\n");
        }
    }

    /*
     * NAME: removeEntry
     * IMPORT(S): set (DSAHashSet)
     * EXPORT(S): NONE
     * PURPOSE: Remove entries from hash tables
     * CREATION: 28/09/2020
     * LAST MODIFICATION: 22/10/2020
     */

    private static void remove(Set<String> set) {
        System.out.println("\nRemove\n");

        String prompt = "Element: ";
        String value = UserInterface.userInput(prompt);
        set.remove(value);
        System.out.println();
    }

    /*
     * NAME: contains
     * IMPORT(S): set (Set)
     * EXPORT(S): NONE
     * PURPOSE: Checks if a user-specified entry is in set
     * CREATION: 22/10/2020
     * LAST MODIFICATION: 22/10/2020
     */

    private static void contains(Set<String> set) {
        System.out.println("\nContains\n");

        String prompt = "Value: ";
        String value = UserInterface.userInput(prompt);
        System.out.println();

        boolean contains = set.contains(value);
        if (contains) {
            System.out.println(value + " is present in the hash set\n");
        }
        else {
            System.out.println(value + " is not present in the hash set\n");
        }
    }

    /*
     * NAME: print
     * IMPORT(S): set (Set)
     * EXPORT(S): NONE
     * PURPOSE: Print Set
     * CREATION: 28/09/2020
     * LAST MODIFICATION: 02/03/2021
     */

    private static void print(Set<String> set) {
        System.out.println("\nPrint\n");

        System.out.println(set);
        System.out.println();
    }
}
