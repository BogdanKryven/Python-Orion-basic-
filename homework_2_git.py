1. Create a folder called cursor_git_hw
mkdir cursor_git_hw

2. cd into the cursor_git_hw folder.
cd cursor_git_hw/


3. Create a file called first.txt.
touch first.txt

4. Add first.txt to the staging area.
git add first.txt

5. Commit with the message "adding first.txt".
git commit -m 'adding first.txt'

6. Check out your commit with git log.
git log

7. Create another file called second.txt.
touch second.txt

8. Add second.txt to the staging area.
git add second.txt

9. Commit with the message "adding second.txt"
git commit -m 'adding second.txt'

10. Remove the first.txt file
rm first.txt
11. Add this change to the staging area
git add first.txt

# OR INSTEAD OF PARAGRAPHS 10 AND 11 USE
10 AND 11
git rm first.txt

12. Commit with the message "removing first.txt"
git commit -m 'removing first.txt'

13. Check out your commits using git log
git log

14. Push your changes to remote
git push

15. Create new branch from master called `first` (without checkouting)
git branch first
git push --set-upstream origin first

16. Create one more branch from master called `second` (with checkouting to it)
git checkout -b second
git push --set-upstream origin second

17. Change the second.txt file with "Hello" string.
subl second.txt  
# OR WE CAN USE   
echo "Hello" > second.txt

18. Stash you changes and checkout to first branch.
git stash
git checkout first 

19. Checkout back and Stash Pop the changes.
git checkout second
git stash pop

20. Add your changes to the staging area
git add second.txt

21. Commit with the message "Changing second.txt".
git commit -m 'Changing second.txt'

22. Push your changes to remote
git push

23. Checkout to first branch.
git checkout first

24. Change the second.txt file with "Cursor" string.
subl second.txt
# OR
echo "Cursor" > second.txt

25. Add your changes to the staging area
git add second.txt

26. Commit with the message "Changing second.txt".
git commit -m 'Changing second.txt'

27. Push your changes to remote
git push

28. Checkout to master branch
git checkout master

29*. Merge the changes from second branch
git merge second

30*. Then merge the changes from first branch
git merge first

31*. Resolve conflict and push the changes to remote
# Відкриваю проект у програмі PyCharm 
# Нажимаю комбінацію клавіш "Double Shift" (Search Everywhere)
# У віконечку прописую слово "merge" 
# У новому вікні прописую "first" і нажимаю "merge"
# У новому вікні знову нажимаю на кнопку "merge" і самостійно вирішую конфлікт
git push