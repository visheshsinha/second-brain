
**S - Single Responsibility Principle**

- A class should have only one reason to change
- If a class has multiple responsibility and changes if any of the responsibilities logic changes, then it's not following the single responsibility principle
- For this we break it up into each class for one responsibility , as in the change in one will not affect the other classes & hence satisfying the Single Responsibility Principle.

**O - Open Close Principle**

- Open for extension but closed for modification
- Any method of a class which is test & live, should not be modified & instead if the requirement comes, it should just be extended - as in - make a interface and implement it from all the cases you want.
- 