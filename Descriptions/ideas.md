# Ideas

* to draw individual cells, just identify the cell as being drawn and include the circle
    ### i.e.
    * cell.drawn = true # has circle
    * cell.drawn = false # no circle
Note: This is now easily possible with the cell for position method

* let user step forward by calling increase_generation n times i.e.:

    ```
    for _ in user_num:
        self.increase_generation()
    ```