from typing import Any, List, Optional, Union
import flet
from flet import (
    Page,
    TextField,
    FloatingActionButton,
    icons,
    Checkbox,
    Column,
    Row,
    CrossAxisAlignment,
    UserControl,
    MainAxisAlignment,
    IconButton,
    colors,
    Tabs,
    Tab,
    Text,
    OutlinedButton
)
from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref


class TodoApp(UserControl):
    def build(self):
        self.txt_tarea = TextField(hint_text="¿Qué necesitas hacer?", expand=True)

        btn_agregar_tarea = FloatingActionButton(
        icon=icons.ADD,
        on_click=self.agregar_tarea_clicked)

        self.col_tareas = Column()
        self.tabs_filter = Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                Tab(text='Todas'),
                Tab(text='Pendientes'),
                Tab(text='Completadas')
            ]
        )

        self.lbl_task_left = Text('0 tareas pendientes')

        col_controles = Column(
            width=600,
            controls=[
                Row(
                    [
                        Text(value='ToDo App',
                        style='headlineMedium')
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        self.txt_tarea,
                        btn_agregar_tarea
                    ],
                ),
                Column(
                    spacing=25,
                    controls=[
                        self.tabs_filter,
                        self.col_tareas,
                        Row(
                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                self.lbl_task_left,
                                OutlinedButton(
                                    text='Eliminar todas',
                                    on_click=self.delete_all_task
                                )
                            ]
                        )
                    ]
                ),
            ]
        )
        return col_controles
    
    def delete_all_task(self, e):
        for t in self.col_tareas.controls:
            self.delete_task(t)
    
    def agregar_tarea_clicked(self,e):
        tarea = Task(self.txt_tarea.value, self.delete_task, self.task_status_changed)
        self.col_tareas.controls.append(tarea)
        self.txt_tarea.value = ""
        self.update()

    def delete_task(self, task):
        self.col_tareas.controls.remove(task)
        self.update()

    def tabs_changed(self, e):
        self.update()

    def update(self):
        status = self.tabs_filter.tabs[self.tabs_filter.selected_index].text

        count = 0

        for t in self.col_tareas.controls:
            t.visible= (
                status == 'Todas'
                or (status == 'Pendientes' and t.completed == False)
                or (status == 'Completadas' and t.completed)
            )
            if not t.completed:
                count += 1

        self.lbl_task_left.value = f'{count} tareas pendientes '

        super().update()

    def task_status_changed(self,e):
        self.update()

class Task(UserControl):
    def __init__(self, nombre_tarea, delete_callback, task_status_changed_callback):
        super().__init__()
        self.completed = False
        self.nombre_tarea = nombre_tarea
        self.delete_callback = delete_callback
        self.task_status_changed_callback = task_status_changed_callback

    def build(self):
        self.chk_tarea = Checkbox(value=False, label=self.nombre_tarea, on_change=self.status_changed)
        self.txt_tarea = TextField(expand=1)
        self.display_view = Row(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.chk_tarea,
                Row(
                    spacing=0,
                    controls=[
                        IconButton(icon=icons.CREATE_OUTLINED,
                        icon_color=colors.PURPLE,
                        tooltip= 'Editar tarea', 
                        on_click=self.btn_edit_clicked),
                        IconButton(icon=icons.DELETE_OUTLINE,
                        icon_color=colors.PURPLE,
                        tooltip='Eliminar tarea',
                        on_click=self.btn_delete_clicked)
                    ]
                )
            ]
        )

        self.edit_view= Row(
            visible=False,
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.txt_tarea,
                IconButton(icon=icons.DONE_OUTLINE_OUTLINED,
                icon_color=colors.PURPLE,
                tooltip='Editar tarea',
                on_click=self.btn_save_clickend)
            ]
        )
        return Column(
            controls=[
                self.display_view,
                self.edit_view
            ]
        )


    def btn_edit_clicked(self, e):
        self.txt_tarea.value = self.chk_tarea.label
        self.display_view.visible=False
        self.edit_view.visible=True
        self.update()

    def btn_delete_clicked(self, e):
        self.delete_callback(self)

    def btn_save_clickend(self,e):
        self.chk_tarea.label = self.txt_tarea.value
        self.display_view.visible=True
        self.edit_view.visible=False
        self.update()

    def status_changed(self, e):
        self.completed = self.chk_tarea.value
        self.task_status_changed_callback(self)

def main(page: Page):

    todo = TodoApp()

    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.add(todo)


flet.app(target=main)
